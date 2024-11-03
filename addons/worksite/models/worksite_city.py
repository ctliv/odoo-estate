from odoo import fields, models, api

class WorksiteCity(models.Model):
    _name = "worksite.city"
    
    city = fields.Char("Comune")
    province = fields.Char("Provincia (sigla)", size=2)

    @api.depends('city', 'province')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{self.city} ({self.province})"
    
