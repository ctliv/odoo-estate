from odoo import fields, models, api

INVOICELINE_TOCHECK = 'tocheck'
INVOICELINE_CHECKED = 'checked'

INVOICELINE_STATUS = [
    (INVOICELINE_TOCHECK, 'Da associare a DDT'),
    (INVOICELINE_CHECKED, 'Associata a DDT')
]

class WorksiteInvoiceLineInh(models.Model):
    _inherit = "account.move.line"

    costPc = fields.Integer("Percentuale costo", min=0, max=100)
    spanAll = fields.Boolean("Dividere su tutti i cantieri attivi", default=False)

    #TODO: Il campo è calcolato in base a ddt_id. Oppure sostituirlo con una classe css apposita in base a ddt_id
    status = fields.Selection(
            string='Stato',
            selection=INVOICELINE_STATUS,
            default=INVOICELINE_TOCHECK,
            required=True,
            copy=False
            )
    
    worksite_id = fields.Many2one('worksite.site')
    ddt_id = fields.Many2one('worksite.ddt')

    #TODO: ddt_id = fields.Many2One('worksite_ddt')

