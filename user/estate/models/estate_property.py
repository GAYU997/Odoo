from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    expected_price = fields.Integer()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available',default='today + relativedelta(month=4)',copy=False)
    selling_price = fields.Float(copy=False,default='50')
    bedrooms = fields.Integer(default='2',readonly=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [('North','North'), ('South','South'),('East','East'),('West','west')])
    Active = fields.Boolean(default=False)
    state = fields.Selection(
       selection = [('New','New'),('Offer Received','Offer Received'),('Offer Accepted','Offer Accepted'),
                    ('Sold and Canceled','Sold and Canceled')])


    #odoo.fields.name.active = True


    #country_id = fields.Many2one('res.country', string='Country', required=True)
   # name = fields.Char(string='State Name', required=True,
           #    help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
   # code = fields.Char(string='State Code', help='The state code.', required=True)

