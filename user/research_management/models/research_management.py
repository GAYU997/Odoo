from odoo import models, fields


class ResearchFields(models.Model):
    _name = "research.fields"
    _description = "Research Management"

    scholar_id = fields.Integer(string='Scholar Id')
    name = fields.Char()
    #scholar_name = fields.Char(string="Firstname")
    middle_name = fields.Char(string="Middlename")
    last_name = fields.Char(string="Lastname")
    sex = fields.Selection(
        selection=[('Male', 'Male'), ('Female', 'Female')])
    age = fields.Integer()
    institute_information = fields.Text()
    other_information = fields.Text()
    related_partner = fields.Many2one('res.partner')
