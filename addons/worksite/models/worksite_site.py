from odoo import fields, models, api

WORKSITE_ACTIVE = 'active'
WORKSITE_SUSPENDED = 'suspended'
WORKSITE_CLOSED = 'closed'
WORKSITE_COMPLETED = 'completed'

WORKSITE_STATUS = [
    (WORKSITE_ACTIVE, 'Attivo'),
    (WORKSITE_SUSPENDED, 'Sospeso'),
    (WORKSITE_CLOSED, 'Chiuso'),
    (WORKSITE_COMPLETED, 'Completato')
]

class WorksiteSite(models.Model):
    _name = "worksite.site"
    _description = "Cantiere di costruzione"
    _order = "name asc"

    name = fields.Char('Nome', required=True)
    image = fields.Image('Immagine')

    attachment_ids = fields.Many2many("ir.attachment", string="Allegati")

    status = fields.Selection(
            string='Stato',
            selection=WORKSITE_STATUS,
            default=WORKSITE_ACTIVE,
            required=True,
            copy=False
            )

    street = fields.Char('Indirizzo')
    street2 = fields.Char('Indirizzo 2')
    zip = fields.Char('CAP', size=5, default='29121')

    city_id = fields.Many2one('worksite.city', string="Comune e Provincia")

    # city = fields.Char('Comune', default='Piacenza')
    # state_id = fields.Many2one('res.country.state', 'Provincia', domain="[('country_id', '=?', country)]", default=379)    
    # country_id = fields.Many2one('res.country', string='Nazione', default=109)

    note = fields.Html('Note')

    invoice_line_ids = fields.One2many('account.move.line', inverse_name='worksite_id', string='Voci fattura')
