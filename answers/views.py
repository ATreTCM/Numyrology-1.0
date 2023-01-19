
from django.shortcuts import render
from django.views.generic import View

from .models import Social_predictions, Spiritual_predictions, Personal_predictions, Comment, Service, Uset
from .service import *
 
class Users_value(View):
    
    template_name  = 'answers/index.html'
    context = {}
    
    def get(self, request):
        self.context['services'] = Service.objects.all()
        self.context['comment'] = Comment.objects.all()
        return render(request, self.template_name, self.context)
       
class Create_users_value(View):
    
    template_name = 'answers/modal.html'
    context = {}
    
    def post(self, request):
        users_value = request.POST
        new = Uset() 
        new.name = users_value['name-input']
        new.born_date = users_value["data-input"]
        prediction = Numirology(new.born_date)
        prediction.template_method()
        new.personal_predictions = prediction.purpose_personal
        new.social_predictions = prediction.social_purpose
        new.spiritual_predictions = prediction.spiritual_purpose
        new.save()
        
        personal_answers = Personal_predictions.objects.get(purpose_personal=new.personal_predictions)
        self.context['personalH'] = personal_answers.header
        self.context['personalC'] = personal_answers.predictions_personal
        self.context['name'] = new.name
        self.context['date'] = new.born_date
        self.context['purpose_personal'] = prediction.purpose_personal
        self.context['social_purpose'] = prediction.social_purpose
        self.context['spiritual_purpose'] = prediction.spiritual_purpose
        self.context['manifestation_channel'] = prediction.manifestation_channel
        self.context['channel_of_intuition'] = prediction.channel_of_intuition
        self.context['recurring_event_channel'] = prediction.recurring_event_channel
        self.context['soul_lesson'] = prediction.soul_lesson
        self.context['birth_canal1'] = prediction.birth_canal1 
        self.context['birth_canal2'] = prediction.birth_canal2 
        self.context['birth_canal3'] = prediction.birth_canal3 
        self.context['birth_canal4'] = prediction.birth_canal4 

        return render(request, self.template_name, self.context)

def error(request):
    return render(request, 'answers/not_found.html')