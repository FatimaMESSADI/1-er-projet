# -*- coding: utf-8 -*-
from odoo import http

# class Voiture(http.Controller):
#     @http.route('/voiture/voiture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/voiture/voiture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('voiture.listing', {
#             'root': '/voiture/voiture',
#             'objects': http.request.env['voiture.voiture'].search([]),
#         })

#     @http.route('/voiture/voiture/objects/<model("voiture.voiture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('voiture.object', {
#             'object': obj
#         })