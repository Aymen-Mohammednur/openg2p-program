from odoo.addons.component.core import AbstractComponent


class ProcessGroupMixin(AbstractComponent):
    _inherit = "process_group.rest.mixin"

    def _process_group(self, group_info):
        res = super()._process_group(group_info)
        if group_info.dict().get("program_memberships", None):
            res["program_registrant_info_ids"] = self._process_registrant_info(
                group_info, target_type="group"
            )
        return res
