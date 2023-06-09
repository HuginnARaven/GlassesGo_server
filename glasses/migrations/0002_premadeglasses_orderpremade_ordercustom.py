# Generated by Django 4.2.1 on 2023-05-28 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremadeGlasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('photo_url', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPremade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('glasses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.premadeglasses')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.frame')),
                ('lens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.lens')),
                ('lens_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.lenscolor')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.material')),
                ('material_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.materialcolor')),
            ],
        ),
    ]
