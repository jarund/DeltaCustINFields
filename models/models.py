# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class add_in_fields_app(models.Model):
#     _name = 'add_in_fields_app.add_in_fields_app'
#     _description = 'add_in_fields_app.add_in_fields_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models


class DeltaInventoy(models.Model):
    _inherit = 'product.template'

    xt_freight_class = fields.Char(string='Freight Class')
    xt_bol_item_desc = fields.Char(string='BOL Item Description')
    xt_bol_class_info = fields.Char(string='BOL Item Class Information')
