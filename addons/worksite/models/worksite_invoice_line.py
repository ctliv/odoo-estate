from odoo import fields, models, api
from odoo.exceptions import ValidationError

INVOICELINE_TOCHECK = 'tocheck'
INVOICELINE_CHECKED = 'checked'

INVOICELINE_STATUS = [
    (INVOICELINE_TOCHECK, 'Da associare a DDT'),
    (INVOICELINE_CHECKED, 'Associata a DDT')
]

class WorksiteInvoiceLineInh(models.Model):
    _inherit = "account.move.line"

    costPc = fields.Integer("Percentuale costo")
    spanAll = fields.Boolean("Dividere su tutti i cantieri attivi", default=False)

    #Il campo è definito dalla presenza del  ddt_id. Oppure sostituirlo con una classe css apposita in base a ddt_id
    status = fields.Selection(
            string='Stato',
            selection=INVOICELINE_STATUS,
            compute="_compute_status"
            # default=INVOICELINE_TOCHECK,
            # required=True,
            # copy=False
            )
    
    worksite_id = fields.Many2one('worksite.site')
    ddt_id = fields.Many2one('worksite.ddt')

    @api.constrains('costPc')
    def _check_selling_price(self):
        for record in self:
            if record.costPc and (record.costPc < 0 or record.costPc > 100):
                raise ValidationError("Percentuale non valida")
            
    @api.depends('ddt_id')
    def _compute_line_count(self):
        for rec in self:
            if rec.ddt_id:
                rec.status = INVOICELINE_CHECKED
            else:
                rec.status = INVOICELINE_TOCHECK

