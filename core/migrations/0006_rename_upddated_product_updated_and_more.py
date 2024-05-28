# Generated by Django 5.0.6 on 2024-05-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category_user_alter_product_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upddated',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'draft'), ('rejected', 'Rejected'), ('disabled', 'Disabled'), ('published', 'Published')], default='in_review', max_length=10),
        ),
    ]