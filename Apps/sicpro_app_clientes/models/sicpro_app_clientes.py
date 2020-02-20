# -*- coding: utf-8 -*-


from odoo.tools import email_re, email_split, UserError
from odoo import api, fields, models, tools, _



class AppClientes(models.Model):
    _name = 'sicpro.app.clientes'
    _order = "id asc"
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _description = 'Aplicación de Clientes'

    name = fields.Char(required=True, string='Nombre', tracking=True, )
    es_entidad = fields.Boolean(string="es_entidad", )
    entidad = fields.Many2one(comodel_name="sicpro.app.clientes", string="Entidad", required=False, )
    tipo_registro = fields.Selection(string="", selection=[('persona', 'Persona'),('entidad', 'Entidad'), ], default='entidad', )
    hijos_ids = fields.One2many(comodel_name="sicpro.app.clientes", inverse_name="entidad", string="Hijos", required=False, )
    etiquetas = fields.Many2many(comodel_name="sicpro.app.clientes.etiquetas", string="Etiquetas", )
    territorio = fields.Many2one(comodel_name="sicpro.nomenclador.territorios", string="Territorio",
                                   required=True, tracking=True,)
    provincia = fields.Many2one(comodel_name="sicpro.nomenclador.provincia", string="Provincia",
                                 required=True, default="", tracking=True, )
    cargo = fields.Char(string="Cargo", required=False, tracking=True, )
    telefono_fijo = fields.Char(string="Teléfono", required=False, tracking=True,  )
    telefono_movil = fields.Char(string="Móvil", required=False, tracking=True, )
    correo = fields.Char(string="Correo", required=False, tracking=True, )
    pagina_web= fields.Char(string="Pagína Web", required=False, tracking=True, )
    observaciones = fields.Text(string="Observaciones", required=False, )
    active = fields.Boolean(string="Activo", default=True, tracking=True, )
    # Todos los campos de imagen están codificados en base64 y son compatibles con PIL
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    #campos redimensionados almacenados (como archivo adjunto) para rendimiento
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

     #Seleccion entre entidad y persona
    @api.onchange('tipo_registro')
    def _onchange_tipo_registro(self):
        if self.tipo_registro == 'entidad':
            self.es_entidad = True
        else:
            self.es_entidad = False

      #devuelve nuevos valores a provincia cuando el territorio ha cambiado
    def _onchange_territorio_values(self, territorio):
        if territorio:
            partner = self.env['sicpro.nomenclador.territorios'].browse(territorio)
            return {'provincia': partner.provincia}
        return {}

    # Al cambiar campo territorio
    @api.onchange('territorio')
    def _onchange_territorio(self):
        values = self._onchange_territorio_values(self.territorio.id if self.territorio else False)
        self.update(values)