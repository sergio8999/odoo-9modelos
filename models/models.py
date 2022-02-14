# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class venta_productos(models.Model):
#     _name = 'venta_productos.venta_productos'
#     _description = 'venta_productos.venta_productos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class producto(models.Model):
	_name = 'venta_productos.producto'
	_description = 'model producto'

	name = fields.Char('refProducto',required=True,unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	descripcion = fields.Char(string='Descripción', required=True)
	precio = fields.Float(string='Precio',required=True,digits=(6, 2))

	#relaciones
	proveedor_id=fields.Many2one('venta_productos.proveedor',string='Id Proveedor')
	lineas_pedidos_ids = fields.One2many('venta_productos.linea_pedido', 'producto_id', string='Lineas pedido')
	almacen_id=fields.Many2one('venta_productos.almacen',string='Id Almacen')

class proveedor(models.Model):
	_name = 'venta_productos.proveedor'
	_description = 'model proveedor'

	name = fields.Char('refProveedor',required=True, unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono', required=True)

	# relaciones
	productos_ids = fields.One2many('venta_productos.producto','proveedor_id',string='Referencia producto')

class pedido(models.Model):
	_name = 'venta_productos.pedido'
	_description = 'model pedido'

	name = fields.Char('nPedido',required=True,unique=True)
	direccion = fields.Char(string='Direccion',required=True)
	fecha_pago = fields.Date(string='Fecha de pago', required=True)

	#relaciones
	cliente_id=fields.Many2one('venta_productos.cliente',string='Cliente')
	lineas_pedidos_ids = fields.One2many('venta_productos.linea_pedido', 'pedido_id', string='Lineas Pedido')

class cliente(models.Model):
	_name = 'venta_productos.cliente'
	_description = 'model cliente'

	name = fields.Char('idCliente',required=True, unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	direccion = fields.Char(string='Direccion', required=True)

	# relaciones
	pedidos_ids = fields.One2many('venta_productos.pedido','cliente_id',string='Referencia cliente')

class linea_pedido(models.Model):
	_name = 'venta_productos.linea_pedido'
	_description = 'model linea_pedido'

	name = fields.Char('idLinea_pedido',required=True,unique=True)
	cantidad = fields.Integer(string='Cantidad', required=True)
	precio = fields.Float(string='Precio',required=True,digits=(6, 2))

	#relaciones
	pedido_id=fields.Many2one('venta_productos.pedido',string='Id Pedido')
	producto_id = fields.Many2one('venta_productos.producto', string='Id Producto')

class almacen(models.Model):
	_name = 'venta_productos.almacen'
	_description = 'model almacen'

	name = fields.Char('idAlmacen',required=True, unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	direccion = fields.Char(string='Direccion', required=True)

	# relaciones
	productos_ids = fields.One2many('venta_productos.producto','almacen_id',string='Productos')
	zona_id = fields.Many2one('venta_productos.producto', string='Cod. Zona')

class zona(models.Model):
	_name = 'venta_productos.zona'
	_description = 'model zona'

	name = fields.Char('idZona',required=True, unique=True)
	ciudad = fields.Char(string='Ciudad',required=True)
	provincia = fields.Char(string='Provincia', required=True)

	# relaciones
	almacenes_ids = fields.One2many('venta_productos.almacen','zona_id',string='Id Almacen')