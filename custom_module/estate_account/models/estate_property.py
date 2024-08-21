from odoo import fields, models, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        # Call the original method

        # Create an invoice for the sold property
        import pdb; pdb.set_trace()
        invoice = self.env['account.move'].create({
            'partner_id': self.offer_ids.filtered(lambda x: x.status == 'accepted').partner_id.id,
            'move_type': 'out_invoice',
            'invoice_date': fields.Date.context_today(self),
            'currency_id': self.env.company.currency_id.id,
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

        return super().action_sold()
