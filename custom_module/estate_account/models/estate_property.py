from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        # Call the original method

        # Create an invoice for the sold property
        invoice = self.env['account.move'].create({
            'partner_id': self.buyer_id.id,
            'journal_id': self.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,
            'invoice_line_ids': [
                Command.create({
                    'name': 'Property Sale: %s' % self.title,
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                }),
                Command.create({
                    'name': 'Administrative Fees',
                    'quantity': 1,
                    'price_unit': 100.00,
                }),
            ],
        })

        import pdb; pdb.set_trace()
        return super().action_sold()
