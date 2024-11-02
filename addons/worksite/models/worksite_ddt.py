from odoo import fields, models, api

DDT_TOCHECK = 'tocheck'
DDT_CHECKED = 'checked'

DDT_STATUS = [
    (DDT_TOCHECK, 'Da associare a fattura'),
    (DDT_CHECKED, 'Associato a fattura')
]

class WorksiteDDT(models.Model):
    _name = "worksite.ddt"
    _description = "Documento di Trasporto emesso da fornitore"

    name = fields.Char('Numero DDT', size=20, required=True)
    date = fields.Date('Data DDT', required=True)
    attachment_binary = fields.Binary('Allegato', copy=False)
    attachment_name = fields.Char('Nome allegato')

    #TODO: Il campo è calcolato in base a invoice_id. Oppure sostituirlo con una classe css apposita in base a invoice_id
    status = fields.Selection(
            string='Stato',
            selection=DDT_STATUS,
            default=DDT_TOCHECK,
            required=True,
            copy=False
            )
    
    invoice_line_ids = fields.One2many('account.move.line', inverse_name='ddt_id', string="Voci fattura")
    
    #invoice_ids implicito, recuperato dalle voci fattura, a loro volta linkate alla fattura