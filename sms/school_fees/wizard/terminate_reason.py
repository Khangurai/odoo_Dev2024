# See LICENSE file for full copyright and licensing details.


from odoo import _, models
from odoo.exceptions import ValidationError


class TerminateReasonFees(models.TransientModel):
    _inherit = "terminate.reason"

    def save_terminate(self):
        """Override method to raise warning when fees payment of student is
        remaining when student is terminated"""
        student = self._context.get("active_id")
        student_rec = self.env["student.student"].browse(student)
        if self.env["student.payslip"].search(
            [
                ("student_id", "=", student_rec.id),
                ("state", "in", ["confirm", "pending"]),
            ]
        ):
            raise ValidationError(
                _(
                    "You can't terminate student because payment of fees of "
                    "student is remaining!"
                )
            )
        return super(TerminateReasonFees, self).save_terminate()
