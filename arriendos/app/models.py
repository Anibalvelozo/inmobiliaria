from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Usuario(models.Model):
    # Relación OneToOne con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return self.user.username


class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region


class Comuna(models.Model):
    comuna = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas', null=True, blank=True)

    def __str__(self):
        return f"{self.comuna} ({self.region.region if self.region else 'Sin Región'})"


class Tipo_inmueble(models.Model):
    TIPO_CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.tipo


class Inmueble(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(Tipo_inmueble, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_bano = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    numero_hab = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Tipo_usuario(models.Model):
    TIPO_CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.tipo


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.usuario.username
