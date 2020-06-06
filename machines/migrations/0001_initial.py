# Generated by Django 2.2.7 on 2019-12-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('Processorspeed', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price', models.IntegerField()),
                ('RAMgb', models.IntegerField()),
                ('HDDgb', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')], max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('TFT', 'TFT'), ('LCD', 'LCD'), ('LED', 'LED')], max_length=20)),
                ('size', models.DecimalField(decimal_places=1, max_digits=4)),
                ('price', models.IntegerField()),
                ('display', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')], max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
