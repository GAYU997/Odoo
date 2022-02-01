from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    product_brand = fields.Many2one('product.brand')
    product_master_type = fields.Selection(
        selection=[('Single_Product', 'Single Product'),
                   ('Branded_Product', 'Branded Product')])


class Brand(models.Model):
    _name = "product.brand"
    _description = "brand"
    name = fields.Char(string="Name")
   # product_brand = fields.Many2one('product.brand')






