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
    invoice_user_id = fields.Many2one('res.users', string='Vendedor', readonly=True)
    fecha_numerico = fields.Integer(string='Fecha en Numero', readonly=True)
    
    def _select(self):
        select_str = super(PosOrderReport, self)._select()
        select_str += """
            
            ,pt.default_code as default_code,
            pt.name as name,
            s.account_move as account_move,
            am.invoice_user_id as invoice_user_id,
            l.price_subtotal_incl as price_subtotal_incl,
            to_char(cast(date_order as date), 'YYYYMMDD')::integer as fecha_numerico
            
            """
        return select_str
    
    def _from(self):
        from_str = super(PosOrderReport, self)._from()
        from_str += """
        LEFT JOIN account_move am ON (s.account_move=am.id)
        LEFT JOIN res_users ru ON (ru.id = am.invoice_user_id)  
            """
        return from_str
        
    
    def _group_by(self):
        group_str = super(PosOrderReport, self)._group_by()
        group_str += """
            ,pt.default_code,
            pt.name,
            am.invoice_user_id,
            l.price_subtotal_incl
            
            """
        return group_str
      