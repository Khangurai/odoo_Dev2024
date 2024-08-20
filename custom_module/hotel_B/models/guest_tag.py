import uuid
from odoo import api, fields, models, _

class GuestTag(models.Model):
    _name = 'guest.tag'
    _description = 'Guest Tag'
    _sql_constraints = [
        ('unique_tag_name', 'unique(name)', 'Name must be unique.'),
        ('check_sequence', 'CHECK(sequence > 0)', 'Sequence must be positive.')
    ]

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True, copy=False)
    color = fields.Integer(string="Color")
    color2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)") % self.name

        default['sequence'] = 10
        return super(GuestTag, self).copy(default)
