# Generated by Django 3.1.2 on 2020-10-22 00:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Cannabis', 'Cannabis'), ('Coco', 'Coco'), ('Cola de Caballo', 'Cola de Caballo'), ('Jalea Real', 'Jalea Real'), ('Maqui y Acai', 'Maqui y Acai'), ('Menta Chocolate', 'Menta Chocolate'), ('Ortiga Romero', 'Ortiga Romero'), ('Palta Oliva', 'Palta Oliva'), ('Argán', 'Argán'), ('Fenix Hair', 'Fenix Hair')], default='Cannabis', max_length=20)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('tipo_producto', models.CharField(choices=[('Tripack', 'Tripack'), ('Bótox', 'Bótox'), ('Spray Termoprotector', 'Spray Termoprotector')], default='Tripack', max_length=20)),
                ('precio', models.IntegerField(default=0)),
                ('aroma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Capilarte1.aroma')),
            ],
            options={
                'ordering': ['tipo_producto'],
            },
        ),
    ]
