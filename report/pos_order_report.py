# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, tools, _

class PosOrderReport(models.Model):
    _inherit = "report.pos.order"
    
    default_code = fields.Char(string='Referencia Producto', readonly=True)
    name = fields.Char(string='Nombre del Producto', readonly=True)
    price_subtotal_incl = fields.Float(string='Sub Total con Impuestos', readonly=True)
    account_move = fields.Many2one('account.move', string='Factura', readonly=True)
    fecha_numerico = fields.Integer(string='Fecha en Numero', readonly=True)
    
    def _select(self):
        select_str = super(PosOrderReport, self)._select()
        select_str += """
            
            ,pt.default_code as default_code,
            pt.name as name,
            s.account_move as account_move,
            l.price_subtotal_incl as price_subtotal_incl,
            to_char(cast(date_order as date), 'YYYYMMDD')::integer as fecha_numerico
            
            """
        return select_str
    
    
    
    def _group_by(self):
        group_str = super(PosOrderReport, self)._group_by()
        group_str += """
            ,pt.default_code,
            pt.name,
            l.price_subtotal_incl
            
            """
        return group_str
      