# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosAcuerdoServicios(models.Model):
    _name = 'sicpro.nomenclador.as'
    _description = 'Nomencladores de Acuerdos de Servicios'

    name = fields.Char(required=True, string='Estado AS')
    descripcion = fields.Char(string="Descripción", required=True,)
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )