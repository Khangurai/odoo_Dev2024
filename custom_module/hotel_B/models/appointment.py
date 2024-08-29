from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class HotelAppointment(models.Model):
    _name = 'hotel.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hotel Appointment'
    _rec_name = 'guest_id'

    guest_id = fields.Many2one('hotel.guest', string='Guest', ondelete='restrict')
    gender = fields.Selection(related='guest_id.gender', readonly=False)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    sequence = fields.Char(string='Sequence', readonly=True, copy=False)
    ref = fields.Char(string='Reference', help="Reference from guest records.")
    note = fields.Html(string='Note')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], default='draft', string="Status", required=True)
    receptionist_id = fields.Many2one('res.users', string='Receptionist', tracking=True)
    items_lines_ids = fields.One2many('appointment.items.lines', 'appointment_id', string="Items Lines")
    hide_sales_price = fields.Boolean(string="Hide Sales Price")

    operation_id = fields.Many2one(comodel_name='hotel.operation', string="Operation")

    @api.onchange('guest_id')
    def _onchange_guest_id(self):
        self.ref = self.guest_id.ref

    def action_test(self):
        print("Button clicked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successful',
                'type': 'rainbow_man',
            }
        }

    def action_draft(self):
        print(self.env.context.get('active_id'))
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('sequence'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('hotel.appointment')
            _logger.info(f"Generated sequence: {vals['sequence']}")
        return super(HotelAppointment, self).create(vals)

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError(_("You can delete appointment only in draft status!"))
        return super(HotelAppointment, self).unlink()

    def name_get(self):
        result = []
        for record in self:
            name = record.sequence or '[No Sequence]'
            result.append((record.id, name))
        return result

class AppointmentItemsLines(models.Model):
    _name = 'appointment.items.lines'
    _description = 'Appointment Items Lines'

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    quantity = fields.Integer(string='Quantity', default="1")
    appointment_id = fields.Many2one('hotel.appointment', string='Appointment')

