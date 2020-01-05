from rest_framework import serializers

from ..models import Subnet, Vlan


class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'

class VlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlan
        fields = '__all__'
