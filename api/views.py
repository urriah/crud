from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .serializers import BuildSerializer
from .models import Build

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/builds/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of builds'
        },
        {
            'Endpoint': '/builds/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single build object'
        },
        {
            'Endpoint': '/builds/create',
            'method': 'POST',
            'body': {'name': "", 'components': {}},
            'description': 'Creates a new build with data sent in post request'
        },
        {
            'Endpoint': '/builds/id/update',
            'method': 'PUT',
            'body': {'name': "", 'components': {}},
            'description': 'Updates an existing build with data sent in put request'
        },
        {
            'Endpoint': '/builds/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing build'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getBuilds(request):
    builds = Build.objects.all()
    serializer = BuildSerializer(builds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBuild(request, pk):
    try:
        build = Build.objects.get(id=pk)
    except Build.DoesNotExist:
        raise Http404("Build not found")
    serializer = BuildSerializer(build, many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createBuild(request): 
    data = request.data
    if 'name' not in data or 'components' not in data:
        return Response({'error': 'Name and components are required'}, status=400)

    build = Build.objects.create(
        name=data['name'],
        components=data['components']
    )
    serializer = BuildSerializer(build, many=False)
    return Response(serializer.data, status=201)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateBuild(request, pk): 
    try:
        build = Build.objects.get(id=pk)
    except Build.DoesNotExist:
        return Response({'error': 'Build not found'}, status=404)

    serializer = BuildSerializer(build, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteBuild(request, pk):
    try:
        build = Build.objects.get(id=pk)
        build.delete()
        return Response({'message': 'Build was deleted successfully'}, status=204)
    except Build.DoesNotExist:
        return Response({'error': 'Build not found'}, status=404)
    