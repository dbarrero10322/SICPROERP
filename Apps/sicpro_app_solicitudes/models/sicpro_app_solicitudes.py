# -*- coding: utf-8 -*-


from odoo.tools import email_re, email_split, UserError
from odoo import api, fields, models, tools, _

# Nombre de la aplicación
app = 'Apps Solicitudes'


class AppSolicitudes(models.Model):
    _name = 'sicpro.app.solicitudes'
    _order = "id asc"
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _description = 'Aplicación de Solicitudes'

    name = fields.Char(required=True, string='Titulo', tracking=True, )
    direccion_territorial = fields.Char(string="Dirección Territorial", required=True, tracking=True, )
    inversionista = fields.Char(string="Inversionista", required=True, tracking=True, )
    pep = fields.Char(string="Pep", required=True, size=10, tracking=True, )
    proceso = fields.Char(string="proceso", required=True, tracking=True, )
    especialidad = fields.Many2one(comodel_name="sicpro.nomenclador.especialidad", string="Especialidad",
        required=True, tracking=True, domain="[('company_id', '=', company_id)]")  # obligo aque salga las especialidades del procesos especifico
    estado = fields.Char(string="Estado", required=True, tracking=True, )
    procede = fields.Char(string="procede", required=True, tracking=True, )
    documentacion = fields.Char(string="Documentación", required=True, tracking=True, )

    fecha_creada_solicitud = fields.Date(string="Fecha Recibida", required=False, )
    fecha_enviada_dpto = fields.Date(string="Enviada al Dpto", required=False, )
    fecha_asignada_especialista = fields.Date(string="Asignada al Especialista", required=False, )
    fecha_convertida_pt = fields.Date(string="Lista para PT", required=False, )
    especialistas = fields.Char(string="Especialistas", required=False, tracking=True, )

    alcance = fields.Text(string="Alcance", required=False, )
    observaciones = fields.Text(string="Observaciones", required=False, )
    anio = fields.Char(string="Año", required=False, default=fields.datetime.today().strftime("%Y"), )  # Devuelvo el año actual
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)  # Devuelvo la compañia actual
    active = fields.Boolean(string="Activo", default=True, tracking=True, )



    # Valido campo presupuesto y mando aviso web_notify de "Proyecto creado"
    #def create(self, vals):
    #    request = super(AppSolicitudes, self).create(vals)
    #    if request.presupuesto != 0:
    #        self.env.user.notify_success(message='El Proyecto ha sido creado correctamente', title=app)
    #    else:
    #        raise UserError(_('Por favor verifique el campo Presupuesto. Valor: '+str(request.presupuesto)))
    #    return request


    # notificacion de "Proyecto creado" a los seguidores: esta se utiliza en las acciones automatizadas del servidor
    #def mensaje_proyecto_creado(self):
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
    #def write(self, vals):
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
