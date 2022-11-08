# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, tools, _

class PosOrder(models.Model):
    _inherit = "pos.order"
    
    info_extra = fields.Char(string='Info Extra') 