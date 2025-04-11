from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    global_tax_id = fields.Many2one('account.tax', string='TVA globale')

    @api.onchange('global_tax_id')
    def _onchange_global_tax_id(self):
        if self.global_tax_id:
            for line in self.order_line:
                line.tax_id = [(6, 0, [self.global_tax_id.id])]
