# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosTrimestres(models.Model):
    _name = 'sicpro.trimestre'
    _description = 'Estado de Trimestres'

    name = fields.Char(required=True, string='Trimestre')
    descripcion = fields.Char(string="Descripción", required=True,)
    active = fields.Boolean(string="Activo", default=True, )