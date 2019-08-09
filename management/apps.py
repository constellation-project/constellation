from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_delete

from . import signals


class management(AppConfig):
    name = "management"

    def ready(self):
        pre_delete.connect(
            signals.pre_delete_interface,
            sender='management.InterfaceDomains'
        )
        post_delete.connect(
            signals.post_delete_interface,
            sender='management.InterfaceDomains'
        )
