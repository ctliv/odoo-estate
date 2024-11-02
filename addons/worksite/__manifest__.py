{
    'name': 'Worksite',
    'version': '1.0',
    'summary': 'Worksite IT Module',
    'author': 'CT-SoftData',
    'description': """
        Reportistica cantieri Barocco Costruzioni Edili S.r.l.
    """,
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'account',
        'l10n_it_edi_ndd'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/worksite_site_views.xml',
        'views/worksite_invoice_views.xml',
        'views/worksite_ddt_views.xml',
        'views/worksite_menus.xml'
    ]
}
