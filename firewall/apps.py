from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FirewallConfig(AppConfig):
    name = "firewall"
    verbose_name = _("firewall")
