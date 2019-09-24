from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_delete
from django.utils.translation import gettext_lazy as _

from . import signals


class ManagementConfig(AppConfig):
    name = "management"
    verbose_name = _("management")

    def ready(self):
        pre_delete.connect(
            signals.pre_delete_interface,
            sender='management.InterfaceDomains'
        )
        post_delete.connect(
            signals.post_delete_interface,
            sender='management.InterfaceDomains'
        )
