from rest_framework import viewsets
from . import models, serializers

class Social_predictionsViewset(viewsets.ModelViewSet):
    queryset = models.Social_predictions.objects.all()
    serializer_class = serializers.Social_predictionsSerializer
    
class Spiritual_predictionsViewset(viewsets.ModelViewSet):
    queryset = models.Spiritual_predictions.objects.all()
    serializer_class = serializers.Spiritual_predictionsSerializer
    
class Personal_predictionsViewset(viewsets.ModelViewSet):
    queryset = models.Personal_predictions.objects.all()
    serializer_class = serializers.Personal_predictionsSerializer
    
class CommentsViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentsSerializer
    
class ServicesViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServicesSerializer

class UsetViewset(viewsets.ModelViewSet):
    queryset = models.Uset.objects.all()
    serializer_class = serializers.UsetSerializer