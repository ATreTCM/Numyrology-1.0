from rest_framework import serializers
from . import models


class Social_predictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Social_predictions
        fields = ('social_purpose', 'header', 'predictions_social')

class Spiritual_predictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spiritual_predictions
        fields = ('spiritual_purpose', 'header', 'predictions_spiritual')

class Personal_predictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Personal_predictions
        fields = ('purpose_personal', 'header', 'predictions_personal')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('name', 'comment', 'avka', 'date_add')
        
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ('header', 'text', 'price')
        
class UsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Uset
        fields = ('name', 'born_date', 'social_predictions', 'spiritual_predictions', 'personal_predictions')

