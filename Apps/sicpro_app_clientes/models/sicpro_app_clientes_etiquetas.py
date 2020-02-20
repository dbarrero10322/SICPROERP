# -*- coding: utf-8 -*-


from odoo.tools import email_re, email_split, UserError
from odoo import api, fields, models, tools, _


class AppClientesEtiquetas(models.Model):
    _name = 'sicpro.app.clientes.etiquetas'
    _order = "id asc"
    _description = 'Etiquetas para la Aplicación de Clientes'

    name = fields.Char(required=True, string='Etiqueta', tracking=True, )
    active = fields.Boolean(string="Activo", default=True, tracking=True, )