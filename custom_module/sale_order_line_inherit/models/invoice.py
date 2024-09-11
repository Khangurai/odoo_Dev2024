from odoo import models, fields, api
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(string='Discount Amount')

