# -*- coding: utf-8 -*-

import time 

from osv import osv, fields
import netsvc
logger = netsvc.Logger()
class report_xml(osv.osv):
    _name = 'ir.actions.report.xml'
    _inherit = 'ir.actions.report.xml'

    _columns = {
        'page_count':fields.char('Page Count', size=128, help="Line count on each page, in format 'first_last_page, first_page, middle_page,last_page', for example,'17,22,26,21'. "),
    }

    def get_page_count(self, cr, user, report_name, context=None):
        res = {'min':17,'first':22,'mid':26,'last':21}
        try:
            ids = self.search(cr, user,[('report_name','=',report_name)],context=context)
            page_cnt = self.read(cr, user, ids, ['page_count'], context=context)
            if page_cnt and page_cnt[0]['page_count']:
                cnts = page_cnt[0]['page_count'].split(',')
                if len(cnts) >= 4:
                    res['min'] = int(cnts[0])
                    res['first'] = int(cnts[1])
                    res['mid'] = int(cnts[2])
                    res['last'] = int(cnts[3])

        except Exception, e:
            pass
        
        return res
report_xml()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: