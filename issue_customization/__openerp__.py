# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-Today OpenERP S.A. (<http://www.openerp.com>).
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
    'name': 'Issue Optimization',
    'version': '1.1',
    'category': '',
    'sequence': 2,
    
    'description': """
Overview:
===============================
* Shows the deadline in issue Form and Kanban views.  The deadline shows in red color in Kanban view in case it has already passed.
* Issues will be sorted by deadline in Kanban view.
* Adds 'Description' in Search view.
* Replaces the 'Worklogs' page in Form view to add 'to_invoice' field.

Assumptions:
===============================
* Modules 'project_issue_sheet' and 'hr_timesheet_invoice' are installed.
    
    """,
    'category': 'Project Issue Management',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'http://www.openerp-asia.net',
    'depends': ['project_issue', 'project_issue_sheet', 'hr_timesheet_invoice'],
    'data': [
        'issue_optimization.xml',
    ],
    
    'installable': True,
    'application': True,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
