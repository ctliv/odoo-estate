from odoo import fields, models, api

INVOICE_TOCHECK = 'tocheck'
INVOICE_CHECKED = 'checked'

INVOICE_STATUS = [
    (INVOICE_TOCHECK, 'Da validare'),
    (INVOICE_CHECKED, 'Validata')
]

class WorksiteInvoiceInh(models.Model):
    _inherit = "account.move"

    docType = fields.Many2one("l10n_it.document.type")

    status = fields.Selection(
            string='Stato',
            selection=INVOICE_STATUS,
            default=INVOICE_TOCHECK,
            required=True,
            copy=False
            )

    #worksite_ddt_ids recuperati implicitamente dalle voci fattura, già linkate ad account.move