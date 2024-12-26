from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Persona
from .serializers import PersonaSerializer




@api_view(['GET'])
def getPersona(request):
    personas = Persona.objects.all()
    serializer = PersonaSerializer(personas, many = True)
    return Response(serializer.data)



@api_view(['POST'])
def addPersona(request):
    serializer = PersonaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
