# Generated by Django 5.0.4 on 2024-05-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_product_latitude_alter_product_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
    ]