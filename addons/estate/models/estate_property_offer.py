from odoo import fields, models

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate.property.offer'

    price = fields.Float("Price", required=True)
    status = fields.Selection(
        string='Offer Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="Select status")
    
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    