# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
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
    'name' : 'Payment Schedule',
    'version' : '1.1',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'http://www.openerp-asia.net',    
    'summary': 'Adds the menu item "Payment Schedule"',
    'description': """
    
Functions:
==========
* Add the menu item "Payment Schedule" which shows all the outstanding AR/AP records.
* Payment Schedule should show accumulated residual amount to facilitate users' projection on cash balance. 

Note:
============
* The new column Begin Balance of the first row is based on sum balance for accounts of type "liquidity" - Identify the period of the latest opening entry and sum up the amount of the relevant account_move_line records whose period is equal to or greater than the identified period.  In case there is no opening entry all the account_move_line records are considered.
* The records of in and out payment are based on account_type ['payable', 'receivable'], and we ignore items from Opening Entries Journal.
   
    """,
    'category': 'Accounting & Finance',
    'sequence': 25,
    'website' : 'http://www.openerp-asia.net',
    'images' : [],
    'depends' : ['account_voucher'],
    'demo' : [],
    'data' : ['account_move_line_view.xml'],
    'test' : [],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
