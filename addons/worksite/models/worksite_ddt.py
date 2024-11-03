from odoo import fields, models, api
# from odoo.addons.project.controllers.project_sharing_chatter import ProjectSharingChatter

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
    ddt_date = fields.Date('Data DDT', required=True)
    ddt_item_count = fields.Integer("Voci DDT", default=0)
    line_count = fields.Integer("Voci fattura", compute="_compute_line_count")

    #TODO: Il campo è calcolato in base a invoice_id. Oppure sostituirlo con una classe css apposita in base a invoice_id
    status = fields.Selection(
            string='Stato',
            selection=DDT_STATUS,
            default=DDT_TOCHECK,
            required=True,
            copy=False
            )
    
    #worksite_ids implicito, recuperato dalle voci fattura
    partner_id = fields.Many2one('res.partner')
    #invoice_ids implicito, recuperato dalle voci fattura, a loro volta linkate alla fattura
    invoice_line_ids = fields.One2many('account.move.line', inverse_name='ddt_id', string="Voci fattura")
    attachment_ids = fields.Many2many("ir.attachment", string="Allegati")

    # attachment_binary = fields.Binary('Allegato', copy=False)
    # attachment_name = fields.Char('Nome allegato')

    @api.depends('name', 'ddt_date')
    def _compute_display_name(self):
        for rec in self:
            if self.name and self.ddt_date:
                rec.display_name = f"{self.name} ({self.ddt_date:%d-%m-%Y})"
            elif self.name:
                rec.display_name = f"{self.name}"

    @api.depends('invoice_line_ids')
    def _compute_line_count(self):
        for rec in self:
            if rec.invoice_line_ids:
                # rec.line_count = len([obj for obj in rec.invoice_line_ids if obj])
                rec.line_count = len(rec.invoice_line_ids)
            else:
                rec.line_count = 0

    # @api.model
    # def _get_thread_with_access(self, thread_id, mode="read", **kwargs):
    #     if project_sharing_id := kwargs.get("project_sharing_id"):
    #         if token := ProjectSharingChatter._check_project_access_and_get_token(
    #             self, project_sharing_id, self._name, thread_id, kwargs.get("token")
    #         ):
    #             kwargs["token"] = token
    #     return super()._get_thread_with_access(thread_id, mode, **kwargs)
