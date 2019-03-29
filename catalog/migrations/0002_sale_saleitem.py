# Generated by Django 2.1.5 on 2019-03-26 18:50

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('purchased', models.DateTimeField(default=None, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7)),
                ('tax', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7)),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7)),
                ('charge_id', models.TextField(default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deleted')], default='A', max_length=1)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='catalog.Sale')),
            ],
            options={
                'ordering': ['product__name'],
            },
        ),
    ]
