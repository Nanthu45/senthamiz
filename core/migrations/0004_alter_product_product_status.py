# Generated by Django 5.0.4 on 2024-06-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_squarefeet_alter_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'draft'), ('disabled', 'Disabled'), ('published', 'Published'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
    ]