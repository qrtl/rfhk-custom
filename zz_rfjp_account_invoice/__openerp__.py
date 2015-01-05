# -*- coding: utf-8 -*-
##############################################################################
#
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
    'name': 'Account Invoice Customization',
    'version': '1.0',
    'author': 'Rooms For (Hong Kong) Limited',
    'category': 'Account',
    'description': """
Affected menu items:
 - Customer Invoices
 - Supplier Invoices

Functions:
 - Sort invoice records by Due Date (ascending)
 - Set default filter to show invoice records with status other than "Done" or "Cancelled"
    """,
    'depends': ['base_setup', 'sale', 'account'],
    'data': [
        'account_invoice_view.xml'
    ],
    'installable': True,
    'active': True,
}