# Generated by Django 2.2.6 on 2019-11-09 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoInstrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='instrumento',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrumento',
            name='precio',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrumento',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
        migrations.AddField(
            model_name='instrumento',
            name='tipoInstrumento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TipoInstrumento'),
        ),
    ]
