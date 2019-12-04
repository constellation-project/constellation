def pre_delete_interface(sender, instance, using, **kwargs):
    instance.a_records.all().delete()
    instance.aaaa_records.all().delete()
    instance.cname_records.all().delete()
    instance.ptr_records.all().delete()
    instance.firewall_layer2.all().delete()
    instance.firewall_layer3.all().delete()
    instance.firewall_layer4.all().delete()

def post_delete_interface(sender, instance, using, **kwargs):
    instance.interface.delete()
