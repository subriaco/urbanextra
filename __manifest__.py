# -*- coding: utf-8 -*-


{
    'name': 'Urban extra',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo reportes Urban',
    'description': """

""",
    'depends': ['point_of_sale','web_dashboard'],
    'data': [
        'views/pos_order_report_view.xml',
        'views/pos_order_view.xml',
    ],
    'assets':{
    },
    'installable': True,
    'auto_install': False,
}
