import openerp.addons.decimal_precision as dp
from osv import osv, fields

class account_invoice(osv.osv):

    def _amount_residual2(self, cr, uid, ids, name, args, context=None):
        if context is None:
            context = {}
        result = {}
        for invoice in self.browse(cr, uid, ids, context=context):
            if invoice.type == 'out_invoice':
                result[invoice.id] = invoice.residual
            else:
                result[invoice.id] = - invoice.residual
        return result

    
    _inherit = 'account.invoice'
    _name = 'account.invoice'
    _order = 'date_due'
    _columns = {
         'residual2': fields.function(_amount_residual2, digits_compute=dp.get_precision('Account'), string='Balance2')
    }
