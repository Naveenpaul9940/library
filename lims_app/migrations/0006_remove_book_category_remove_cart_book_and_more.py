# Generated by Django 5.1.1 on 2024-10-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0005_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
