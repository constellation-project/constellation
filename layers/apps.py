from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LayersConfig(AppConfig):
    name = "layers"
    verbose_name = _("network layers")
