from openerp.osv import fields, osv



#class sale_order(osv.osv):
#    def new_get_order(self, cr, uid, ids, context=None):
#        result = {}
#        for field in self.pool.get('sale.order').browse(cr, uid, ids, context=context):
#            result[field.order_id.id] = True
#        return result.keys()
#    
#    _inherit = 'sale.order.line'
#    _columns = {
#                'date_order': fields.date('Date', required=True, readonly=True, select=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
#                }
#sale_order()



#class new_sale_order_tree(osv.osv):
#    _name = 'new_sale_order_tree'
#    _inherit = 'res.company'
#    _columns = {
#                'phone': fields.char('Phone'),
                
                
#                }
#new_sale_order_tree()

#class new_sale_order_tree(osv.osv):
       
#    def new_get_order(self, cr, uid, ids, context=None):
#        result = {}
#        for field in self.pool.get('sale.order').browse(cr, uid, ids, context=context):
#            result[field.sale.order] = True
#        return result.keys()    

#    value = {
#              'standard_price': self.pool.get('product.template').browse(cr,uid,context=context).standard_price
#              }
    
#    _name = 'new_sale_order_tree'


class new_sale_order_tree(osv.osv):
    
        
    def _get_order_user(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id] = line.order_id.user_id.id
        return result.keys()
       
    def _get_order_order_date(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.date_order
        return result.keys()
    
    def _get_order_due_date(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.commitment_date
        return result.keys()
    
    def _get_order_ref(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.client_order_ref
        return result.keys()
    
    def _get_order_curr(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.currency_id
        return result.keys()
    
    def _get_order_curr_rate(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.currency_id.rate
        return result.keys()
    
    def _get_order_num(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.order_id.name
        return result.keys()
    
    def _get_order_cost(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order.id]=line.product_id.standard_price
        return result.keys()
  
   
    def multi_unicost_qty(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            res[record.id] = record.uni_cost * record.rate * record.product_uom_qty
        return res
    
    def base_amt(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            res[record.id] = record.price_subtotal * record.rate
        return res
    
    def gross_profit(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            res[record.id] = record.base_amt - record.cost_amt
        return res
    
    def profit(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.browse(cr, uid, ids,context):
            if record.cost_amt:
                res[record.id] = record.gross_profit / record.cost_amt
            else:
                res[record.id] = '-'
        return res
    
    
#  def _get_order_subtotal(self, cr, uid, ids, context=None):
#      result = {}
##      for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
##          result[line.order.id]=line.order_id.amount_untaxed 
##      return result.keys()
          
#    _name = 'new_sale_order_tree'
    _inherit = 'sale.order.line'
    _columns = {
                
                'user_id': fields.related('order_id', 'user_id', relation='res.users', type='many2one', string=u'Salesperson'),
                'date_order': fields.related('order_id','date_order',type='date',string=u'Order Date'),
                'client_order_ref': fields.related('order_id','client_order_ref',type='char',string=u'Customer Reference'),
                'commitment_date': fields.related('order_id','commitment_date',type='date',string=u'Commitment Date'),
                'currency_id': fields.related('order_id','currency_id',relation='res.currency', type='many2one',string=u'Currency'),
                'rate': fields.related('order_id','currency_id','rate',type='float',relation='res.currency',string=u'Currency Rate'),
                'order_name': fields.related('order_id', 'name',type='char', string=u'Number'),
                'uni_cost':fields.related('product_id','standard_price',relation='product.template',type='float',string=u'Cost'),
                'cost_amt':fields.function(multi_unicost_qty, type='float',string=u'Total Cost'),
                'base_amt':fields.function(base_amt, type='float', string=u'Base Amt'),
                'gross_profit':fields.function(gross_profit, type='float', string=u'Gross Profit'),
                'profit':fields.function(profit, type='char', string=u'Profit%'),
                
                
 #              'amount_untaxed':fields.related('order_id','amount_untaxed',type='float',string=u'Subtotal'),
                
                
                
                }
new_sale_order_tree()

#class sale_order_dates1(osv.osv):
#    _inherit = 'sale.order.line'
#    def _get_commitment_date(self, cr, uid, ids, name, arg, context=None):
#        res = {}
#        dates_list = []
#        for order in self.browse(cr, uid, ids, context=context):
#            dates_list = []
#            for line in order.order_line:
#                dt = datetime.strptime(order.date_order, '%Y-%m-%d') + relativedelta(days=line.delay or 0.0)
#                dt_s = dt.strftime('%Y-%m-%d')
#                dates_list.append(dt_s)
#            if dates_list:
#                res[order.id] = min(dates_list)
#        return res

#    _columns = {
#        'commitment_date': fields.function(_get_commitment_date, store=True, type='date', string='Commitment Date', help="Committed date for delivery."),
    
    
#    } 
    
#sale_order_dates1()   


