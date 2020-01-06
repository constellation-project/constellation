from rest_framework import serializers

from ..models import Interface, Machine, Subnet, Vlan


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    interfaces = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Machine
        fields = '__all__'

class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'

class VlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlan
        fields = '__all__'
