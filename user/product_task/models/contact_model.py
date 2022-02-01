from odoo import models, fields


class ContactDetails(models.Model):
    _inherit = 'res.partner'
    is_prime_customer = fields.Boolean()

