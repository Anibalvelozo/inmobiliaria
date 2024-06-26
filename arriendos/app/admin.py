from django.contrib import admin
from .models import Tipo_inmueble,Tipo_usuario, Usuario, Comuna,Region,Perfil, Inmueble
# Register your models here.
admin.site.register(Tipo_inmueble)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Perfil)
admin.site.register(Inmueble)