# -*- coding: utf-8 -*-
from odoo import tools
from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    # dejan_tarimas = fields.Boolean(string="Dejan Tarimas", default=False)
    # flete_externo = fields.Boolean(string="Flete externo", default=False)
    # pagan_tarimas = fields.Boolean(string="Pagan Tarimas", default=False)
    # pagan_maniobras = fields.Boolean(string="Pagan maniobras", default=False)
    # l10n_mx_edi_usage = fields.Selection([
    #     ('G01', 'Acquisition of merchandise'),
    #     ('G02', 'Returns, discounts or bonuses'),
    #     ('G03', 'General expenses'),
    #     ('I01', 'Constructions'),
    #     ('I02', 'Office furniture and equipment investment'),
    #     ('I03', 'Transportation equipment'),
    #     ('I04', 'Computer equipment and accessories'),
    #     ('I05', 'Dices, dies, molds, matrices and tooling'),
    #     ('I06', 'Telephone communications'),
    #     ('I07', 'Satellite communications'),
    #     ('I08', 'Other machinery and equipment'),
    #     ('D01', 'Medical, dental and hospital expenses.'),
    #     ('D02', 'Medical expenses for disability'),
    #     ('D03', 'Funeral expenses'),
    #     ('D04', 'Donations'),
    #     ('D05', 'Real interest effectively paid for mortgage loans (room house)'),
    #     ('D06', 'Voluntary contributions to SAR'),
    #     ('D07', 'Medical insurance premiums'),
    #     ('D08', 'Mandatory School Transportation Expenses'),
    #     ('D09', 'Deposits in savings accounts, premiums based on pension plans.'),
    #     ('D10', 'Payments for educational services (Colegiatura)'),
    #     ('P01', 'To define'),
    # ], 'Usage', default='P01',
    #     help='Used in CFDI 3.3 to express the key to the usage that will '
    #     'gives the receiver to this invoice. This value is defined by the '
    #     'customer. \nNote: It is not cause for cancellation if the key set is '
    #     'not the usage that will give the receiver of the document.')
    # l10n_mx_edi_payment_method_id = fields.Many2one('l10n_mx_edi.payment.method', string="Forma de pago")

# class SaleOrder(models.Model):
#   _inherit = 'sale.order'

#   dejan_tarimas_ven = fields.Boolean(string="Dejan Tarimas", readonly=True)
#   flete_externo_ven = fields.Boolean(string="Flete externo", readonly=True)
#   pagan_tarimas_ven = fields.Boolean(string="Pagan Tarimas", readonly=True)
#   pagan_maniobras_ven = fields.Boolean(string="Pagan maniobras", readonly=True)

#   @api.onchange('partner_id')
#   def onchange_valor_contactos(self):
#     if self.partner_id.dejan_tarimas == True:
#       self.dejan_tarimas_ven = True
#     else:
#       self.dejan_tarimas_ven = False
#     if self.partner_id.flete_externo == True:
#       self.flete_externo_ven = True
#     else:
#       self.flete_externo_ven = False
#     if self.partner_id.pagan_tarimas == True:
#       self.pagan_tarimas_ven = True
#     else:
#       self.pagan_tarimas_ven = False
#     if self.partner_id.pagan_maniobras == True:
#       self.pagan_maniobras_ven = True
#     else:
#       self.pagan_maniobras_ven =  False

# class AccountInvoice(models.Model):
#   _inherit = 'account.invoice'

#   @api.onchange('partner_id')
#   def onchange_partner_id(self):
#     if self.type == 'out_refund':
#       self.l10n_mx_edi_usage = self.partner_id.l10n_mx_edi_usage
#       self.l10n_mx_edi_payment_method_id = self.partner_id.l10n_mx_edi_payment_method_id
#     else:
#       self.l10n_mx_edi_payment_method_id = self.partner_id.l10n_mx_edi_payment_method_id

class StockPicking(models.Model):
  _inherit = "stock.picking"

  @api.onchange('move_ids_without_package')
  def onchange_stock_quant(self):
    for line in self.route_moves:
      ruta = self.env['stock.quant'].search([('product_id','=', line.product_id.id),('location_id','=',self.location_dest_id.id)])
      line.product_uom_qty = ruta.quantity

class MotivoStockScrap(models.Model):
  _name = 'add.motivo'

  name = fields.Char(string="Motivo", required=True)

class StockScraoInherit(models.Model):
  _inherit = 'stock.scrap'

  motivo = fields.Many2one('add.motivo', string="Motivo")

class ReportMermas(models.Model):
  _name = "mermas.report"
  _auto =False

  producto = fields.Char('Producto', readonly=True)
  fecha = fields.Date('Fecha', readonly=True)
  motivo = fields.Char('Motivo',readonly=True)
  ubicacion = fields.Char('Ubicacion', readonly=True)

  sabor = fields.Many2one('taste.product')
  clase = fields.Many2one('class.product')
  presentacion = fields.Many2one('presentation.product')
  marca = fields.Many2one('brand.product')


  def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
    with_ = ("WITH %s" % with_clause) if with_clause else ""

    select_ = """
        pt.name as producto,
        am.name as motivo,
        ss.date_expected as fecha,
        concat(sl2.name,'/',sl.name) as ubicacion,
        pt.taste_product as sabor,
        pt.clase_prod as clase,
        pt.presentation_prod as presentacion,
        pt.brand_product as marca,
        ss.id
    """

    for field in fields.values():
      select_ += field

    from_ = """
        stock_scrap ss
          left join product_product pp on (pp.id=ss.product_id)
          left join product_template pt on (pt.id = pp.product_tmpl_id)
          left join add_motivo am on (am.id = motivo)
          left join stock_location sl on sl.id = ss.location_id
          left join stock_location sl2 on sl2.id = sl.location_id
        %s
    """ % from_clause

    groupby_ = """
        pt.name,
        am.name,
        pt.taste_product,
        pt.clase_prod,
        pt.presentation_prod,
        pt.brand_product,
        sl2.name,
        sl.name,
        ss.id
        %s
    """ % (groupby)

    return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)
  @api.model_cr
  def init(self):
    self._table = 'mermas_report'
    tools.drop_view_if_exists(self.env.cr, self._table)
    self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))