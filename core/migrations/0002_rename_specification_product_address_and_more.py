# Generated by Django 5.0.4 on 2024-06-10 05:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='specification',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='cmda_approved',
            field=models.BooleanField(default=False, help_text='Check if the product is CMDA approved'),
        ),
        migrations.AddField(
            model_name='product',
            name='dtcp_approved',
            field=models.BooleanField(default=False, help_text='Check if the product is DTCP approved'),
        ),
        migrations.AddField(
            model_name='product',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, help_text='Latitude in decimal degrees', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, help_text='Longitude in decimal degrees', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='special_features',
            field=models.TextField(blank=True, help_text='Enter special features separated by commas', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(default='product category', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('published', 'Published'), ('draft', 'draft'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='core.product'),
        ),
    ]
