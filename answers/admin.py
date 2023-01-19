from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Social_predictions, Spiritual_predictions, Personal_predictions, Comment, Service, Uset

class Social_predictionsAdmin(TranslationAdmin):
    
    list_display = (
        'social_purpose',
        'header',
        'predictions_social'
        )
    
class Spiritual_predictionsAdmin(TranslationAdmin):
    
    list_display = (
        'spiritual_purpose',
        'header', 
        'predictions_spiritual'
        )

class Personal_predictionsAdmin(TranslationAdmin):
    
    list_display = (
        'purpose_personal',
        'header',
        'predictions_personal'
        )
class CommentAdmin(TranslationAdmin):
    
    list_display = (
        'name',
        'comment',
        'avka',
        'date_add'
        )
class ServiceAdmin(TranslationAdmin):
    
    list_display = (
        'header',
        'text',
        'like_view',
        'price'
        )
    
class UsetAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'born_date',
        'social_predictions',
        'spiritual_predictions',
        'personal_predictions',
        'date_add'
        )


    list_filter = (
        'date_add',
    )
    
    search_fields = (
        'date_add',
    )

admin.site.register(Social_predictions, Social_predictionsAdmin)
admin.site.register(Spiritual_predictions, Spiritual_predictionsAdmin)
admin.site.register(Personal_predictions, Personal_predictionsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Uset, UsetAdmin)

