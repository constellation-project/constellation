from rest_framework import serializers

from ..models import Interface, Machine, Subnet, Vlan, VlanSubnets


class InterfaceSerializer(serializers.ModelSerializer):
    ip_addresses = serializers.StringRelatedField(many=True)
    subnets = serializers.StringRelatedField(many=True)

    class Meta:
        model = Interface
        fields = ['mac_address', 'subnets', 'ip_addresses']

class MachineSerializer(serializers.ModelSerializer):
    interfaces = InterfaceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Machine
        fields = ['name', 'owner', 'description', 'interfaces']

class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = ['name', 'prefix', 'length']

class VlanSubnetsSerializer(serializers.ModelSerializer):
    subnets = SubnetSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = VlanSubnets
        fields = ['subnets']

class VlanSerializer(serializers.ModelSerializer):
    subnets = VlanSubnetsSerializer(
        read_only=True,
    )

    class Meta:
        model = Vlan
        fields = ['name', 'identifier', 'identifier2', 'subnets']
