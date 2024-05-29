# Generated by Django 5.0.4 on 2024-05-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, help_text='Latitude in decimal degrees', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, help_text='Longitude in decimal degrees', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('draft', 'draft'), ('rejected', 'Rejected'), ('published', 'Published')], default='in_review', max_length=10),
        ),
    ]