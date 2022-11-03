# Generated by Django 3.2 on 2022-11-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='category',
            field=models.CharField(choices=[('item', 'item'), ('badge', 'badge')], default='item', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('item', 'item'), ('badge', 'badge')], default='item', max_length=200),
        ),
    ]