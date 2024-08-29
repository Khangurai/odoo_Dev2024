from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer(string="Cancel Days", config_parameter='hotel_B.cancel_days')
