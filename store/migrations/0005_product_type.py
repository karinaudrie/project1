# Generated by Django 4.0 on 2022-03-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_digital_product_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('always available', 'Always Available'), ('custom', 'Custom')], max_length=20, null=True),
        ),
    ]
