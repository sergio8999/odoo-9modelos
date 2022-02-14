# -*- coding: utf-8 -*-
# from odoo import http


# class VentaProductos(http.Controller):
#     @http.route('/venta_productos/venta_productos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/venta_productos/venta_productos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('venta_productos.listing', {
#             'root': '/venta_productos/venta_productos',
#             'objects': http.request.env['venta_productos.venta_productos'].search([]),
#         })

#     @http.route('/venta_productos/venta_productos/objects/<model("venta_productos.venta_productos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('venta_productos.object', {
#             'object': obj
#         })
