# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jarochito(models.Model):
    _inherit = "res.partner"

    cod_comprador = fields.Selection([('1','Alberto Burgos'),
                                      ('2','Angela Ramos'),
                                      ('3','Esmeralda Romero'),
                                      ('4','Bonifilio Matías'),
                                      ('5','Cesar Prado'),
                                      ('6','Yesenia Huerta'),
                                      ('7','Daniel Rosas'),
                                      ('8','Gerardo Díaz M'),
                                      ('9','Jose Arturo Rendon Rivera'),
                                      ('10','Juan Ramon Rangel'),
                                      ('11','Jorge Sicardo'),
                                      ('12','Juan Carlos Tello'),
                                      ('13','Mauricio Peña'),
                                      ('14','Manuel Sanchez'),
                                      ('15','Oscar Moreno'),
                                      ('16','Omar Torres'),
                                      ('17','Ricardo Cozar'),
                                      ('18','Raul Cozar'),
                                      ('19','Jose S. Ros Garcia'),
                                      ('20','Varios')], string="Código de comprador")
    cod_almacen = fields.Selection([('1','General'),('2','Refacción')], string="Código de almacen")
    group_contable_pro = fields.Text(string="Grupo contable proveedores")
    group_contable_neg = fields.Text(string="Grupo contable Negocio")

    dejan_tarimas = fields.Boolean(string="Dejan Tarimas", default=False)
    flete_externo = fields.Boolean(string="Flete externo", default=False)
    pagan_tarimas = fields.Boolean(string="Pagan Tarimas", default=False)
    pagan_maniobras = fields.Boolean(string="Pagan maniobras", default=False)


class SaleOrder(models.Model):
  _inherit = 'sale.order'

  dejan_tarimas_ven = fields.Boolean(string="Dejan Tarimas", readonly=True)
  flete_externo_ven = fields.Boolean(string="Flete externo", readonly=True)
  pagan_tarimas_ven = fields.Boolean(string="Pagan Tarimas", readonly=True)
  pagan_maniobras_ven = fields.Boolean(string="Pagan maniobras", readonly=True)

  @api.onchange('partner_id')
  def onchange_valor_contactos(self):
    if self.partner_id.dejan_tarimas == True:
      self.dejan_tarimas_ven = True
    else:
      self.dejan_tarimas_ven = False
    if self.partner_id.flete_externo == True:
      self.flete_externo_ven = True
    else:
      self.flete_externo_ven = False
    if self.partner_id.pagan_tarimas == True:
      self.pagan_tarimas_ven = True
    else:
      self.pagan_tarimas_ven = False
    if self.partner_id.pagan_maniobras == True:
      self.pagan_maniobras_ven = True
    else:
      self.pagan_maniobras_ven =  False