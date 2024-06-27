# services.py

from .models import Inmueble, Usuario, Region, Comuna, Tipo_inmueble, Tipo_usuario

# Función para crear un nuevo inmueble
def crear_inmueble(usuario, tipo_inmueble, comuna, region, nombre, m2_construido, numero_bano, numero_hab, direccion):
    """
    Crea un nuevo objeto Inmueble y lo guarda en la base de datos.

    Args:
    - usuario: Instancia de User que representa al usuario propietario del inmueble.
    - tipo_inmueble: Instancia de Tipo_inmueble que define el tipo de inmueble.
    - comuna: Instancia de Comuna que representa la comuna donde está ubicado el inmueble.
    - region: Instancia de Region que representa la región donde está ubicado el inmueble.
    - nombre: Nombre del inmueble.
    - m2_construido: Área construida del inmueble en metros cuadrados.
    - numero_bano: Número de baños del inmueble.
    - numero_hab: Número de habitaciones del inmueble.
    - direccion: Dirección física del inmueble.

    Returns:
    - Nuevo objeto Inmueble creado y guardado en la base de datos.
    """
    nuevo_inmueble = Inmueble.objects.create(
        usuario=usuario,
        tipo_inmueble=tipo_inmueble,
        comuna=comuna,
        region=region,
        nombre=nombre,
        m2_construido=m2_construido,
        numero_bano=numero_bano,
        numero_hab=numero_hab,
        direccion=direccion
    )
    return nuevo_inmueble


# Función para obtener todos los inmuebles
def obtener_todos_inmuebles():
    """
    Retorna todos los objetos Inmueble almacenados en la base de datos.

    Returns:
    - QuerySet con todos los inmuebles almacenados.
    """
    return Inmueble.objects.all()


# Función para actualizar un inmueble existente
def actualizar_inmueble(inmueble_id, m2_construido, numero_bano, numero_hab):
    """
    Actualiza los datos de un inmueble existente en la base de datos.

    Args:
    - inmueble_id: ID del inmueble que se desea actualizar.
    - m2_construido: Nueva área construida del inmueble en metros cuadrados.
    - numero_bano: Nuevo número de baños del inmueble.
    - numero_hab: Nuevo número de habitaciones del inmueble.

    Returns:
    - Objeto Inmueble actualizado si se encontró y modificó correctamente, None si no se encontró.
    """
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.m2_construido = m2_construido
        inmueble.numero_bano = numero_bano
        inmueble.numero_hab = numero_hab
        inmueble.save()
        return inmueble
    except Inmueble.DoesNotExist:
        return None


# Función para borrar un inmueble
def borrar_inmueble(inmueble_id):
    """
    Elimina un inmueble de la base de datos según su ID.

    Args:
    - inmueble_id: ID del inmueble que se desea eliminar.

    Returns:
    - True si se eliminó correctamente, False si el inmueble no existe.
    """
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        inmueble.delete()
        return True
    except Inmueble.DoesNotExist:
        return False
