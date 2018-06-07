# Generated by Django 2.0.5 on 2018-06-06 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contratos',
            fields=[
                ('idcon', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fecha', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('idinven', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paquetes',
            fields=[
                ('idpaq', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='trabajadores',
            fields=[
                ('idtrabajador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='idPersona',
        ),
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.DeleteModel(
            name='persona',
        ),
        migrations.AddField(
            model_name='contratos',
            name='idpaq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paquetes'),
        ),
    ]