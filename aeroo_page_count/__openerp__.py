# -*- coding: utf-8 -*-
##############################################################################
#
#    Custom Module for TAOLight 
#    for use in
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'AEROO REPORT Page Count',
    'version': '0.1',
    'category': 'Generic Modules/report',
    'description': """
    Add a field on aeroo report object: Page Count. Set lines count on each type of page, in format 'first_last_page, first_page, middle_page,last_page', for example,'17,22,26,21'.
    """,
    'author': 'OSCG',
    'website': 'http://www.oscg.com.hk',
    'depends': ['report_aeroo'],
    'web_depends': [],
    'init_xml': [],
    'update_xml': ['report_xml_view.xml',
                  ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
