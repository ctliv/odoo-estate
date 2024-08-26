from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Reale Estate Property definition"
    _order = "id desc"
    active = fields.Boolean('Active', default=True)

    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description', required=True, translate=True)
    postcode = fields.Char('Postcode', required=False)
    # date_availability = fields.Date('Availability Date', required=True, default=lambda self: fields.Datetime.add( fields.Datetime.today(), months=3), copy=False)
    date_availability = fields.Date('Availability Date', required=True, default=fields.Date.add(fields.Date.today(), months=3), copy=False)
    expected_price = fields.Float('Expected Price', required=False)
    selling_price = fields.Float('Selling Price', required=False, copy=False, readonly=True)
    bedrooms = fields.Integer('Bedrooms', required=True, default=2)
    living_area = fields.Integer('Living Area', required=True, default=0)
    facades = fields.Integer('Facades', required=True, default=0)
    garage = fields.Boolean('Garage', required=True, default=False)
    garden = fields.Boolean('Garden', required=True, default=False)
    garden_area = fields.Integer('Garden Area', required=True, default=0)
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')],
        help="Select garden orientation")
    state = fields.Selection(
            string='State',
            selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
            default='new',
            required=True,
            copy=False
            )
    
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", inverse_name="property_id", string="Offers")
    
    type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Partner")
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
