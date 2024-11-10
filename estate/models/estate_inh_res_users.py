from odoo import fields, models

class InheritedResUsers(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many("estate.property", inverse_name="salesperson_id", domain=('state','in',['new','offer_received']))
    