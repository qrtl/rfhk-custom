{
    'name': 'Web RFHk',
    'category': 'Hidden',
    'version': '7.0.1.0',
    'description':
        """
OpenERP Web core module.
========================

This module provides the core of the OpenERP Web Client.
        """,
    'category': 'Web',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'http://www.openerp-asia.net',
    'depends': ['web'],
    'auto_install': True,
    'qweb' : [
        "static/src/xml/*.xml",
        ],
    
}