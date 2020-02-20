# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosSolicitudes(models.Model):
    _name = 'sicpro.nomenclador.estados.solicitudes'
    _description = 'Estado de Solicitudes'

    name = fields.Char(required=True, string='Estado')
    descripcion = fields.Char(string="Descripción", required=True,)
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )