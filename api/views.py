from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            'body': {'body':""},
            'description': 'Creates new build with data sent in post request'
        },
        {
            'Endpoint': '/builds/id/update',
            'method': 'PUT',
            'body': {'body':""},
            'description': 'Creates an existing build with data sent in put request'
        },
        {
            'Endpoint': '/builds/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting build'
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
    build = Build.objects.get(id=pk)
    serializer = BuildSerializer(build, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createBuild(request): 
    data = request.data

    build = Build.objects.create(
        body=data['body']
    )
    serializer = BuildSerializer(build, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBuild(request, pk): 
    data = request.data

    build = Build.objects.get(id=pk)
    serializer = BuildSerializer(build, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBuild(request, pk):
    build = Build.objects.get(id=pk)
    build.delete()
    return Response('Build was deteled')
