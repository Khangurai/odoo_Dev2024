from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hotel Guest'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string ='Gender', tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hotel.appointment', string='Appointments')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('guest.tag', string='Tags')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count',store=True)
    parent = fields.Many2one('hotel.guest', string='Parent')
    marital_status = fields.Char(string='Marital Status')
    partner_name = fields.Char(string='Partner Name')
    is_visible = fields.Boolean(compute='_compute_is_visible')

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hotel.appointment'].search_count([('guest_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError(("The entered date of birth is in the future."))

    @api.model
    def create(self, vals):
        if not vals.get('ref'):
            vals['ref']=self.env['ir.sequence'].next_by_code('hotel.guest')
        return super(HotelGuest, self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref']=self.env['ir.sequence'].next_by_code('hotel.guest')
        return super(HotelGuest, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def name_get(self):
        # return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
