
# encoding: utf-8

#from osv import osv
import netsvc
from report import report_sxw
from report.report_sxw import rml_parse
import time
import netsvc
logger = netsvc.Logger()
LINES_PER_PAGE = 12


class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.so_seq = 0
        report_obj = self.pool.get('ir.actions.report.xml')
        rs = report_obj.get_page_count(cr, uid, name, context=context)
        self.page_cnt = {'min':rs['min'],'first':rs['first'],'mid':rs['mid'],'last':rs['last']}
        self.localcontext.update({
            'time':time,
            'get_pages':self.get_pages,
            'get_address':self.get_address,
            })
    
    def get_address(self,obj):
        res_partner = self.pool.get('res.partner')
        addresses = res_partner.address_get(self.cr, self.uid, [obj.partner_id.id], ['default', 'delivery', 'invoice'])
        addr_invoice_id = addresses['invoice'] or addresses['default']
        addr_delivery_id = addresses['delivery'] or addresses['default']
        invoice_obj = res_partner.browse(self.cr,self.uid,addr_invoice_id)
        delivery_obj = res_partner.browse(self.cr,self.uid,addr_delivery_id)
        return {
            'invoice':{'street':invoice_obj.street or '','street2':invoice_obj.street2 or '','phone':invoice_obj.phone or '','fax':invoice_obj.fax or '','name':invoice_obj.name},
            'delivery':{'street':delivery_obj.street or '','street2':delivery_obj.street2 or '','phone':delivery_obj.phone or '','fax':delivery_obj.fax or '','name':delivery_obj.name},
            }

    def new_page(self,n,pn,max):
        if n==max:
            return True
        left = max - n + pn
        if left > self.page_cnt['last'] and left <= self.page_cnt['mid'] and pn == left-1:
            return True
        if left > self.page_cnt['last'] and left > self.page_cnt['mid'] and pn == self.page_cnt['mid']:
            return True
        if left <= self.page_cnt['last'] and pn == self.page_cnt['last']:
            return True
            
        return False

    def get_pages(self,obj):
        res = []
        seq = 0
        total_ln = []
        for line in obj.invoice_line:
            ln={}
            ln['note'] = line.product_id and line.product_id.name or ''
            ln['qty'] = line.quantity or 0.00
            ln['uos_id'] = line.uos_id.name or ''
            ln['price_unit'] = line.price_unit or 0.00
            ln['line_total'] = line.price_unit * line.quantity
            ln['seq'] = '%s' % (seq+1,)
            total_ln.append(ln)
            seq += 1
            if line.name:
                note_lines = line.name.split('\n')
                for nl in note_lines:
                    if not ln['note']:
                        ln['note'] = nl
                    else:
                        line = {'seq': '', 'note':nl, 'qty': '', 'price_unit': '', 'line_total': '', 'uos_id':''}
                        total_ln.append(line)
                line = {'seq': ' ', 'note':' ','qty': '', 'price_unit': '', 'line_total': '', 'uos_id':''}
                if seq < len(obj.invoice_line):
                    total_ln.append(line)
        
        page = {}
        a_cnt = 0
        p_cnt = 0
        pn = 0
        max = len(total_ln)
        for ln in total_ln:
            if not page.get('lines',False):
                page['lines'] = []
            page['lines'].append(ln)
            a_cnt += 1
            p_cnt += 1
            if self.new_page(a_cnt,p_cnt,max):
                pn += 1
                page['pn'] = pn
                page['ln_cnt'] = p_cnt
                res.append(page.copy())
                p_cnt = 0
                page={}
        
        if res:
            page_last = res[-1]
            page_last['last'] = True
        
        ln={'note':' ','qty': '', 'price_unit': '', 'line_total': '', 'seq': ' ', 'uos_id':''}
        for p in res:
            if p['pn'] != pn:
                p['continue'] = "Cont. on Page %d" % (p['pn']+1,)
            else:
                p['continue'] = " "
            p['pn'] = 'Page %s of %s' % (p['pn'],pn)

            blank_line = 0
            if p.get('last',False):
                blank_line = self.page_cnt['last'] - p['ln_cnt']
            else:
                blank_line = self.page_cnt['mid'] - p['ln_cnt']
            for i in range(blank_line):
                p['lines'].append(ln)
            if p.get('lines',False) and len(p['lines']) > 0 :
                p['lines'][-1]['last_ln'] = 1
        return res