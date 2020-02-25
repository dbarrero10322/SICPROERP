# -*- coding: utf-8 -*-


from odoo.tools import email_re, email_split, UserError
from odoo import api, fields, models, tools, _

# Nombre de la aplicación
app = 'Apps Solicitudes'


class AppSolicitudesInversionistas(models.Model):
    _name = 'sicpro.app.solicitudes.inversionistas'
    _order = "prioridad desc, id asc"
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _description = 'Aplicación de Solicitudes'

    name = fields.Char(required=True, string='Titulo', tracking=True, )
    territorio = fields.Many2one(comodel_name="sicpro.nomenclador.territorios", string="Territorio",
                                 required=True, tracking=True, )
    provincia = fields.Many2one(comodel_name="sicpro.nomenclador.provincia", string="Provincia",
                                required=True, default="", tracking=True, )
    prioridad = fields.Selection(string='Prioridad', selection=[('1', '1'), ('2', '2'), ], index=True, tracking=True, )
    cliente = fields.Many2one(comodel_name="sicpro.app.clientes", string="Clientes", required=True,
                              domain="[('tipo_registro', '=', 'persona')]", )
    pep = fields.Char(string="Pep", required=True, size=10, tracking=True, )
    proceso = fields.Char(string="proceso", required=True, tracking=True, )

    # obligo a que salga las especialidades del procesos especifico
    especialidad = fields.Many2one(comodel_name="sicpro.nomenclador.especialidad", string="Especialidad",
                                   required=True, tracking=True, domain="[('company_id', '=', company_id)]")

    procede = fields.Char(string="procede", required=True, tracking=True, )
    documentacion = fields.Char(string="Documentación", required=True, tracking=True, )

    # Devuelvo la fecha actual
    fecha_creada_solicitud = fields.Date(string="Fecha Recibida", required=False,
                                         default=fields.datetime.today(), )

    alcance = fields.Text(string="Alcance", required=False, )
    observaciones = fields.Text(string="Observaciones", required=False, )

    # Devuelvo el año actual
    anio = fields.Char(string="Año", required=False, default=fields.datetime.today().strftime("%Y"), )

    # Devuelvo la compañia actual
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    active = fields.Boolean(string="Activo", default=True, tracking=True, )

    # devuelve nuevos valores a provincia y territorio cuando el cliente ha cambiado
    def _onchange_clientes_values(self, cliente):
        if cliente:
            valor = self.env['sicpro.app.clientes'].browse(cliente)
            return {'provincia': valor.provincia,
                    'territorio': valor.territorio,
                    }
        return {}

    # Al cambiar campo Cliente
    @api.onchange('cliente')
    def _onchange_cliente(self):
        values = self._onchange_clientes_values(self.cliente.id if self.cliente else False)
        self.update(values)

    # Valido campo presupuesto y mando aviso web_notify de "Proyecto creado"
    # def create(self, vals):
    #    request = super(AppSolicitudes, self).create(vals)
    #    if request.presupuesto != 0:
    #        self.env.user.notify_success(message='El Proyecto ha sido creado correctamente', title=app)
    #    else:
    #        raise UserError(_('Por favor verifique el campo Presupuesto. Valor: '+str(request.presupuesto)))
    #    return request

    # notificacion de "Proyecto creado" a los seguidores: esta se utiliza en las acciones automatizadas del servidor
    # def mensaje_proyecto_creado(self):
    #    display_msg = """<strong>Nuevo proyecto creado</strong>
    #                      <br/>
    #                      <strong>Proyecto:</strong> """ + str(self.name) + """
    #                      <br/>
    #                      <strong>Código:</strong> """ + str(self.codigo) + """
    #                      <br/>
    #                      <strong>Especialidad:</strong> """ + str(self.especialidad.name) + """
    #                      <br/>
    #                      <strong>Pep:</strong> """ + str(self.pep) + """
    #                      <br/> """
    #    self.message_post(body=display_msg, type="notification", subtype="mt_comment")

    # Aviso y notificacion de "Proyecto modificado"
    # def write(self, vals):
    #    request = super(AppSolicitudes, self).write(vals)

    #    if self.active:
    #        # Aviso web_notify de Proyecto modificado
    #        self.env.user.notify_warning(message='El Proyecto ha sido modificado correctamente', title=app)

    # notificacion Proyecto modificado a los seguidores
    #        display_msg = "<strong>Proyecto Modificado</strong>"
    #        self.message_post(body=display_msg, type="notification", subtype="mt_comment")
    #    else:
    #        usuario = self.env.user.name

    # Aviso web_notify de Proyecto Archivado
    #        self.env.user.notify_danger(
    #                message='El Proyecto ha sido archivado correctamente', title=app)

    # notificacion Proyecto archivado a los seguidores
    #        display_msg = """<strong>Proyecto Archivado</strong>
    #                      <br/>
    #                      <strong>Usuario:</strong> """ + str(usuario) + """
    #                      <br/> """
    #        self.message_post(body=display_msg, type="notification", subtype="mt_comment")
    #    return request
