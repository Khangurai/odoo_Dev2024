from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    name = fields.Char(string='Name', required=True)

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

    def action_confirm(self):
        print("Success......................")
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

# class SaleOrderInherit(models.Model):
#     _name = 'sale.order.inherit'
#     _inherit = []
#
#     name = fields.Char(string='Name', required=True)
#
#     confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
#
# class SaleOrderDelegate(models.Model):
#     _name = 'sale.order.delegate'
#     _inherits = {'estate.property': 'estate_id'}
#
#     estate_id = fields.Many2one(comodel_name='estate.property')
