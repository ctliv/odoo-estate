from odoo import api, fields, models, tools
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate.property.offer"
    _order = "price desc"

    price = fields.Float("Price", required=True)
    status = fields.Selection(
        string="Offer Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        help="Select status",
    )

    validity = fields.Integer("Validity (days)", default=7)
    deadline = fields.Date(
        "Deadline", compute="_compute_deadline", inverse="_inverse_deadline"
    )

    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    property_type_id = fields.Many2one("estate.property.type", related="property_id.type_id", store=True)

    _sql_constraints = [("price", "CHECK (price > 0)", "Price must be above zero")]

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.deadline = record.create_date + timedelta(days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            if record.deadline:
                record.validity = (record.deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self:
            if record.property_id.state == "offer_accepted":
                raise UserError("Already accepted an offer for this property")

            if record.property_id.state in ("sold", "canceled"):
                raise UserError("Cannot accept an offer for a Sold/Canceled Property")

            if not record.price:
                raise UserError("An offer without a price cannot be accepted!")

            record.status = "accepted"
            record.property_id.state = "offer_accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

        return True

    def action_refuse(self):
        for record in self:
            if record.property_id.state in ("sold", "canceled"):
                raise UserError("Cannot refuse an offer for a Sold/Canceled Property")
            record.status = "refused"
            record.property_id.state = "offer_received"

        return True

    def _check_property_state(record):
        if not record.property_id.state or record.property_id.state == "new":
            print("Setting property state...")
            record.property_id.state = "offer_received"

    # def create(self, vals):
    #     record = super(PropertyOffer, self).create(vals)
    #     PropertyOffer._check_property_state(self)
    #     return record

    def write(self, vals):
        PropertyOffer._check_property_state(self)
        return super(PropertyOffer, self).write(vals)

    @api.constrains("price")
    def _check_price(self):
        for record in self:
            if (
                tools.float_compare(
                    record.price,
                    record.property_id.expected_price * 0.9,
                    precision_digits=1,
                )
                < 0
            ):
                raise ValidationError(
                    "The price cannot be less than 90% of expected_price"
                )
