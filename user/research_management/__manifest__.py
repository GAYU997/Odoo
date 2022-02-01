{
    'name': 'Research Management',
    'depends': ['base',
                'sale',
                'contacts'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/research_menu_action.xml',
        'views/book_reservation_action.xml',
        'views/product_cust_views.xml',
        'views/research_menu.xml',


    ],
}