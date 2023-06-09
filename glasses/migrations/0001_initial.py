# Generated by Django 4.2.1 on 2023-05-14 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('photo_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frame_lens', to='glasses.frame')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frame_material', to='glasses.frame')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('photo_url', models.CharField(max_length=255)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_color', to='glasses.material')),
            ],
        ),
        migrations.CreateModel(
            name='LensColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('photo_url', models.CharField(max_length=255)),
                ('lens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lens_color', to='glasses.lens')),
            ],
        ),
    ]
