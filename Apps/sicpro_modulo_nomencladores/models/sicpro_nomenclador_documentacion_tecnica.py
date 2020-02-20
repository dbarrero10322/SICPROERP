# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosDocumentacionTecnica(models.Model):
    _name = 'sicpro.nomenclador.documentacion.tecnica'
    _description = 'Documentación Técnica'

    name = fields.Char(required=True, string='Documento')
    descripcion = fields.Char(string="Descripción", required=True,)
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )