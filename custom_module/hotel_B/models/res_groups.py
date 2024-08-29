from odoo import api, models

class GroupsView(models.Model):
    _inherit = 'res.groups'

    @api.model
    def get_application_groups(self, domain):
        # Overridden in order to remove 'Show Full Accounting Features' and
        # 'Show Full Accounting Features - Readonly' in the 'res.users' form view to prevent confusion
        group_warning_account = self.env.ref('account.group_warning_account', raise_if_not_found=False)
        if group_warning_account and group_warning_account.category_id.xml_id == 'base.module_category_hidden':
            domain += [('id', '!=', group_warning_account.id)]
        group_private_address = self.env.ref('base.group_private_addresses', raise_if_not_found=False)
        if group_private_address and group_private_address.category_id.xml_id == 'base.module_category_hidden':
            domain += [('id', '!=', group_private_address.id)]
        return super().get_application_groups(domain)