# -*- coding: utf-8 -*-
from odoo import http

# class Jarochito(http.Controller):
#     @http.route('/jarochito/jarochito/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jarochito/jarochito/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jarochito.listing', {
#             'root': '/jarochito/jarochito',
#             'objects': http.request.env['jarochito.jarochito'].search([]),
#         })

#     @http.route('/jarochito/jarochito/objects/<model("jarochito.jarochito"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jarochito.object', {
#             'object': obj
#         })