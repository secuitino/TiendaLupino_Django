# Generated by Django 2.2.6 on 2019-11-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaCuerdas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
    ]