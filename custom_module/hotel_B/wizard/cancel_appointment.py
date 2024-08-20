from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime
from odoo.exceptions import ValidationError

try:
    class CancelAppointmentWizard(models.TransientModel):
        _name = 'cancel.appointment.wizard'
        _description = 'Cancel Appointment Wizard'

        @api.model
        def default_get(self, fields):
            res = super(CancelAppointmentWizard, self).default_get(fields)
            res['cancellation_date'] = datetime.date.today()
            res['appointment_id'] = self.env.context.get('active_id')
            return res


        appointment_id = fields.Many2one('hotel.appointment', string='Appointment')
        reason = fields.Text(string='Reason')
        cancellation_date = fields.Date(string='Cancellation Date')
        state = fields.Selection([
            ('draft', 'Draft'),
            ('cancel', 'Cancelled'),
        ], string='Status', default='draft')

        def action_cancel(self):
            # for rec in self:
            #     if rec.appointment_id:
            #         rec.appointment_id.state = 'cancel'  # Ensure that you are updating the correct model
            #         rec.state = 'ca ncel'
            #     else:
            #         raise UserError("No appointment selected.")
            if self.appointment_id.booking_date == fields.Date.today():
                raise ValidationError(_('Sorry, cancellation is not allowed on the same day of booking date'))
            return

except Exception as e:
    print(e)