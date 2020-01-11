from django.db import models
from polymorphic.models import PolymorphicModel


class Product(models.Model):

    PAYER_TYPES = [
        ('all', 'All'),
        ('mem', 'Member'),
        ('org', 'Organization'),
        ('cus', 'Custom')
    ]

    name = models.CharField(max_length=255)
    #currency = models.CharField(max_length=3, default='EUR', editable=False)
    price = models.BigIntegerField()
    payer_type = models.CharField(max_length=3, choices=PAYER_TYPES)

    class Meta:
        unique_together = ('name', 'payer_type')

class InvoiceProducts(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='+')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='+')
    number = models.SmallIntegerField()
    price = models.BigIntegerField(editable=False)

class Invoice(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(
        Product,
        through=InvoiceProducts,
        through_fields=('invoice','product')
    )

class MemberInvoice(Invoice):
    payer = models.ForeignKey('member.Member', on_delete=models.PROTECT, related_name='invoices')

class MembershipInvoice(MemberInvoice):
    membership = models.OneToOneField('member.Membership', on_delete=models.PROTECT, related_name='invoice')

class AccessInvoice(MemberInvoice):
    member = models.ForeignKey('member.Member', on_delete=models.PROTECT, related_name='+')

class OrganizationInvoice(Invoice):
    payer = models.ForeignKey('member.Organization', on_delete=models.PROTECT, related_name='invoices')

class CustomInvoice(Invoice):
    payer = models.TextField()
