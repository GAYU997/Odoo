from odoo import models, fields


class ContactDetails(models.Model):
    _inherit = 'res.partner'
    is_scholar = fields.Boolean()

    def get_scholar(self):
        return{
            'res_model':'book.reservation',
            'type': 'ir.actions.act_window',
            'view_mode':'form',
            'view_type':'form',
            'view_id':
                self.env.ref("research_management.book_reservation_action_form").id,

        }


class Product(models.Model):
    _inherit = 'product.template'
    is_book = fields.Boolean()


class Sales(models.Model):
    _inherit = 'sale.order'
    book_reservation = fields.Many2one('book.reservation')
