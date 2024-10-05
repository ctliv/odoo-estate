from odoo import api, fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name asc"

    name = fields.Char("Property Type Name", required=True)
    sequence = fields.Integer("Sequence", default=1, help="Order sequence")
    active = fields.Boolean("Active", default=True)
    property_ids = fields.One2many("estate.property", inverse_name="type_id")
    offer_ids = fields.One2many(
        "estate.property.offer", "property_type_id"
    )
    offer_count = fields.Integer("Offers", compute="_compute_offer_count")

    _sql_constraints = [("unique_type", "unique(name)", "Type already exists.")]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
