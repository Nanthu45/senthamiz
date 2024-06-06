# Generated by Django 5.0.4 on 2024-06-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_product_cmda_approved_alter_product_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='CMDA_approved',
            new_name='cmda_approved',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('published', 'Published'), ('rejected', 'Rejected'), ('draft', 'draft')], default='in_review', max_length=10),
        ),
    ]
