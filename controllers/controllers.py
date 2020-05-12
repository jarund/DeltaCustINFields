# -*- coding: utf-8 -*-
# from odoo import http


# class AddInFieldsApp(http.Controller):
#     @http.route('/add_in_fields_app/add_in_fields_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_in_fields_app/add_in_fields_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_in_fields_app.listing', {
#             'root': '/add_in_fields_app/add_in_fields_app',
#             'objects': http.request.env['add_in_fields_app.add_in_fields_app'].search([]),
#         })

#     @http.route('/add_in_fields_app/add_in_fields_app/objects/<model("add_in_fields_app.add_in_fields_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_in_fields_app.object', {
#             'object': obj
#         })
