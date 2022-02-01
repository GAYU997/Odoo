from odoo import models, fields


class ResearchFields(models.Model):
    _name = "book.reservation"
    _description = "Book Reservation"

    scholar_id = fields.Many2one('res.partner')
    Responsible = fields.Char(string='Responsible', related='scholar_id.name')
    books = fields.Many2many('product.template')
