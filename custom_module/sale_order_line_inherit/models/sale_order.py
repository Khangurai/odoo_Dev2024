from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_float = fields.Float(string='Discount Amount')

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'discount_float')
    def _compute_amount(self):
        res = super()._compute_amount()
        for line in self:
            if line.discount_float:
                line.price_subtotal = line.price_subtotal - line.discount_float
        return res

    # def _prepare_invoice(self):
    #     invoice_vals = super()._prepare_invoice()
    #     invoice_vals['discount_amount'] = self.discount_float
    #     return invoice_vals

    def _prepare_invoice_line(self, **optional_values):
        """
            If the sale order line isn't linked to a sale order which already have a default analytic account,
            this method allows to retrieve the analytic account which is linked to project or task directly linked
            to this sale order line, or the analytic account of the project which uses this sale order line, if it exists.
        """
        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        if self.discount_float:
            values.update({'discount_amount': self.discount_float})
        return values

