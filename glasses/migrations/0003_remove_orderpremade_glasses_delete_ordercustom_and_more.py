# Generated by Django 4.2.1 on 2023-05-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0002_premadeglasses_orderpremade_ordercustom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpremade',
            name='glasses',
        ),
        migrations.DeleteModel(
            name='OrderCustom',
        ),
        migrations.DeleteModel(
            name='OrderPremade',
        ),
    ]