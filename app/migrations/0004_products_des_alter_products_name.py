# Generated by Django 5.1 on 2024-08-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='des',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
