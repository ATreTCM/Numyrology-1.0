from modeltranslation.translator import translator, TranslationOptions
from .models import Social_predictions, Spiritual_predictions, Personal_predictions, Comment, Service

class Social_predictionsTranslationOptions(TranslationOptions):
    fields = (
        'header', 
        'predictions_social'
        )

class Spiritual_predictionsTranslationOptions(TranslationOptions):
    fields = (
        'header', 
        'predictions_spiritual'
        )

class Personal_predictionsTranslationOptions(TranslationOptions):
    fields = (

        'header', 
        'predictions_personal'
        )

class CommentTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'comment', 
        )
    
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'text',
        'like_view', 
        )
    
translator.register(Social_predictions, Social_predictionsTranslationOptions)
translator.register(Spiritual_predictions, Spiritual_predictionsTranslationOptions)
translator.register(Personal_predictions, Personal_predictionsTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
translator.register(Service, ServiceTranslationOptions)