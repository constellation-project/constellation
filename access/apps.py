from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccessConfig(AppConfig):
    name = "access"
    verbose_name = _("access")
