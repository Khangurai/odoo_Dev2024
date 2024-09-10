from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    discount_amount = fields.Float(string='Discount Amount')

