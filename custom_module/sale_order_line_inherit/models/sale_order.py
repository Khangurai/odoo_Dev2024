from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_float = fields.Float(string='Discount Amount')

    @api.depends('product_id', 'product_uom', 'product_uom_qty', 'discount_float')
    def _compute_price_unit(self):
        res = super()._compute_price_unit()
        for line in self:
            if line.discount_float:
                line.price_unit = line.price_unit - line.discount_float
        return res

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['discount_amount'] = self.discount_float
        return invoice_vals