from .models import Pelicula, PeliculaFavorita
from .serializers import PeliculaSerializer, PeliculaFavoritaSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PeliculaViewSet(viewsets.ModelViewSet):
  queryset = Pelicula.objects.all()
  serializer_class = PeliculaSerializer

  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['titulo', 'estreno']
  ordering_fields = ['favoritos']

class MarcarPeliculaFavorita(views.APIView): # Es una vista de la API genérica
  authentication_classes = [TokenAuthentication] # La autenticación va a ser de tipo token
  permission_classes = [IsAuthenticated] # El usuario para poder acceder a esta vista y marcar películas favoritas tiene que estar autenticado

  # POST -> Se usa para crear un recurso sin un identificador
  # PUT -> Se usa para crear/reemplazar un recurso con un identificador

  def post(self, request): # Request va a tener información de la petición y del usuario que está autenticado a partir del token que definimos arriba (TokenAuthentication)

    pelicula = get_object_or_404(
      Pelicula, id=self.request.data.get('id', 0)
    )

    favorita, created = PeliculaFavorita.objects.get_or_create(
      pelicula=pelicula, usuario=request.user
    ) # Si no encuentra la película, la crea, y si la encuentra, la desmarca como favorita

    # Por defecto suponemos que se crea bien
    content = {
      'id': pelicula.id,
      'favorita': True
    }

    # Si no se ha creado es que ya existe, entonces borramos el favorito
    if not created:
      favorita.delete()
      content['favorita'] = False

    return Response(content)
  
class ListarPeliculasFavoritas(views.APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  # GET -> Se usa para hacer lecturas

  def get(self, request):

    peliculas_favoritas = PeliculaFavorita.objects.filter(
      usuario=request.user)
    serializer = PeliculaFavoritaSerializer(
      peliculas_favoritas, many=True)

    return Response(serializer.data)