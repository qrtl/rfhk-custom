# -*- encoding: utf-8 -*-

{
    'name': 'ATON report',
    'version': '1.0',
    "category" : "Generic Modules/Report",
    'description': """
        ATON report
     """,
    'author': 'OSCG',
    'depends': ['base','report_aeroo','sale','stock','purchase','aeroo_page_count'],
    'init_xml': [],
    'update_xml': [
        'aton_report.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False
}

