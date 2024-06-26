# Generated by Django 4.2 on 2024-06-27 04:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Departamento', 'Departamento'), ('Casa', 'Casa'), ('Parcela', 'Parcela')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Arrendador', 'Arrendador'), ('Arrendatario', 'Arrendatario')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_usuario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('m2_construido', models.FloatField()),
                ('numero_bano', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('numero_hab', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_inmueble')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunas', to='app.region'),
        ),
    ]
