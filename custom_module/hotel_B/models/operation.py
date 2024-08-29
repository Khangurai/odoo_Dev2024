from odoo import api, models, fields

class HotelOperation(models.Model):
    _name = 'hotel.operation'

    _description = 'Hotel Operation'

    name = fields.Char(string='Name')
    doctor_id = fields.Many2one('res.users', string='Doctor')

    description = fields.Char(string='Description')

    reference_record = fields.Reference(string='Reference Record', selection=[('hotel.guest', 'Guest'),
                                                               ('hotel.appointment', 'Appointments')])
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:
            args += ['|', ('name', operator, name), ('description', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        # return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
        return [(record.id, "{1} [{0}]".format(record.name, record.description)) for record in self]

    @api.model
    def name_create(self, name):
        return self.create({'description': name}).name_get()[0]