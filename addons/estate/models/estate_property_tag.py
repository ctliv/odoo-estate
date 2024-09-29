from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate.property.tag'
    _order="name asc"

    name = fields.Char("Tag", required=True)
    color = fields.Integer(string="Color")

    property_ids = fields.Many2many("estate.property", string="Properties")

    _sql_constraints = [
        ('unique_type', 'unique(name)', "Tag already exists.")
    ]
