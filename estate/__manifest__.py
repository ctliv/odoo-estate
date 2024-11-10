{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real estate test Module',
    'author': 'Real Estate Ltd',
    'description': """
        Real Estate Module
    """,
    'installable': True,
    'application': True,
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_inh_res_users.xml',
        'views/estate_menus.xml'
    ]
}
