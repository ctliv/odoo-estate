from odoo import fields, models, api

class WorksiteCity(models.Model):
    _name = "worksite.city"

    city = fields.Char("Comune")
    province = fields.Char("Provincia (sigla)", size=2)

    def __str__(self):
        return f"{self.city} ({self.province})"

