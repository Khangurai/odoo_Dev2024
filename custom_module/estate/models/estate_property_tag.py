from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = 'name asc'

    name = fields.Char(string="Name",required=True)
    color = fields.Integer(string="Color")
    properties = fields.Many2many('estate.property' , 'tags_id', string="Properties")

    _sql_constraints = [
        ('name', 'unique(name)', 'Property tag name must be unique.'),

    ]