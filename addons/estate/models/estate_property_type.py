from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = "name asc"

    name = fields.Char('Property Type Name', required=True)
    active = fields.Boolean('Active', default=True)
    property_id = fields.One2many("estate.property", "type_id")

    _sql_constraints = [
        ('unique_type', 'unique(name)', "Property type already exists.")
    ]
