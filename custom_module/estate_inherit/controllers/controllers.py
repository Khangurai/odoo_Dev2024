# -*- coding: utf-8 -*-
# from odoo import http


# class EstateInherit(http.Controller):
#     @http.route('/estate_inherit/estate_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate_inherit/estate_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate_inherit.listing', {
#             'root': '/estate_inherit/estate_inherit',
#             'objects': http.request.env['estate_inherit.estate_inherit'].search([]),
#         })

#     @http.route('/estate_inherit/estate_inherit/objects/<model("estate_inherit.estate_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate_inherit.object', {
#             'object': obj
#         })

