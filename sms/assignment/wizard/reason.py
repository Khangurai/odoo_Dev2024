# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class RejectReason(models.TransientModel):
    """Defining TransientModel for Reason of Rejection Details."""

    _name = "reject.reason"
    _description = "Reason of Rejection Details"

    reasons = fields.Text(
        "Reject Reason", help="Enter assignment reject reason here"
    )

    def save_reason(self):
        """Method to write reason in assignment model from wizard"""
        student_assignment = self.env["school.student.assignment"]
        for rec in self:
            if self.env.context.get("active_id"):
                student_assignment.search(
                    [("id", "=", self.env.context.get("active_id"))], limit=1
                ).write(
                    {"state": "reject", "rejection_reason": rec.reasons or ""}
                )
        return True
