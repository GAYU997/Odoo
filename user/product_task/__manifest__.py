{
    'name': ' Product Task',
    'depends': ['base',
                'contacts',
                'sale',
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/views.xml',
        'views/orderline_views.xml',
        'data/brand.xml',
    ]
}
