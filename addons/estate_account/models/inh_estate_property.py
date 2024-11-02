from odoo import models

class InheritedEstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sell(self):
        print("Passing here...")

        for record in self:
            record.create_invoice()

        return super().action_sell()

    def create_invoice(self):
        print("Passing also here...")
        return


