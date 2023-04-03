from .models import Pelicula, PeliculaFavorita

from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pelicula
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'

class PeliculaFavoritaSerializer(serializers.ModelSerializer):

  pelicula = PeliculaSerializer()
  # Vamos a serializar el campo película utilizando el serializados que definimos arriba por defecto. Así podremos devolver dentro de lo que son las películas favoritas las películas con todos sus campos.

  class Meta:
    model = PeliculaFavorita
    fields = ['pelicula'] # Solo le decimos que serialice el campo película con el serializador que indicamos arriba