# -*- coding: utf-8 -*-
# from odoo import http


# class HotelBInheritence(http.Controller):
#     @http.route('/hotel_b_inheritence/hotel_b_inheritence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_b_inheritence/hotel_b_inheritence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_b_inheritence.listing', {
#             'root': '/hotel_b_inheritence/hotel_b_inheritence',
#             'objects': http.request.env['hotel_b_inheritence.hotel_b_inheritence'].search([]),
#         })

#     @http.route('/hotel_b_inheritence/hotel_b_inheritence/objects/<model("hotel_b_inheritence.hotel_b_inheritence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_b_inheritence.object', {
#             'object': obj
#         })
