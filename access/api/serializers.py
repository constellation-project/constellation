from rest_framework import serializers

from ..models import Switch, Port
from layers.api.serializers import InterfaceSerializer, VlanSerializer


class PortSerializer(serializers.ModelSerializer):
    vlans = VlanSerializer(
        many=True,
        read_only=True,
    )
    interface = InterfaceSerializer(
        read_only=True,
    )
    port = serializers.StringRelatedField()
    room = serializers.StringRelatedField()

    class Meta:
        model = Port
        fields = ['module', 'number', 'vlans', 'interface', 'port', 'room']


class SwitchSerializer(serializers.ModelSerializer):
    interfaces = InterfaceSerializer(
        many=True,
        read_only=True,
    )
    ports = PortSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Switch
        fields = ['name', 'model', 'interfaces', 'ports']
