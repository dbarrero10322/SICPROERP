# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosClavesHorasLabor(models.Model):
    _name = 'sicpro.nomenclador.claves.hl'
    _description = 'Nomencladores de las claves de HL'

    name = fields.Char(required=True, string='Claves')
    descripcion = fields.Char(string="Descripción", required=True,)
    active = fields.Boolean(string="Activo", default=True, )