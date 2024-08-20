from odoo import models, fields

class PlaygroundItem(models.Model):
    _name = 'playground.item'
    _description = 'Playground Item'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
