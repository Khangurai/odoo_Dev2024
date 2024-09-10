# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderLineInherit(http.Controller):
#     @http.route('/sale_order_line_inherit/sale_order_line_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_line_inherit/sale_order_line_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_line_inherit.listing', {
#             'root': '/sale_order_line_inherit/sale_order_line_inherit',
#             'objects': http.request.env['sale_order_line_inherit.sale_order_line_inherit'].search([]),
#         })

#     @http.route('/sale_order_line_inherit/sale_order_line_inherit/objects/<model("sale_order_line_inherit.sale_order_line_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_line_inherit.object', {
#             'object': obj
#         })

