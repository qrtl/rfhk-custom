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
    'name': 'Releasing',
    'version': '1.1',
    'author': 'Rooms For (Hong Kong) Ltd T/A OSCG',
    'website': 'http://www.open-asia.net',
    'category': 'Project Management',
    'sequence': 8,
    
    'depends': [
        "project",
        "project_issue",
        
     
    ],
    'description': """
1. regard Releasing as the last procedure of each task & issue.
2. define workflow in Releasing, each releasing need to be approved by technical manager & project manager.
2. add 'Releasing' button to project/task/issue form view, which link to page you can create releasing information.


    """,
    'data': [
        'releasing.xml',
        'workflow.xml',
        'release_data.xml',
        'security/releasing_security.xml',
        'security/ir.model.access.csv',

        
    ],
    
    'installable': True,
   
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
