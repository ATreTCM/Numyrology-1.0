from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import Social_predictions, Spiritual_predictions, Personal_predictions, Comments, Services, Uset
from .forms import UsetForm
from .service import *


class Comments_detail(DetailView):
    """Отзыв на услуги"""
    model = Comments
    template_name = ''
    context_object_name = 'comment'
    raise_exception = True


class Service_detail(DetailView):
    """Услуга и цена"""
    model = Services
    template_name = ''
    context_object_name = 'comment'
    raise_exception = True


class Comments_list(ListView):
    """Список комментариев"""
    model = Comments
    template_name = ''
    context_object_name = 'comments'
    raise_exception = True


class Services_list(ListView):
    """Список услуг и цен"""
    model = Services
    template_name = ''
    context_object_name = 'services'
    raise_exception = True


def create_users_value(request):
    """Расчет предназначения пользователя"""
    if request.method == 'POST':
        value_form = UsetForm(request.POST)
        if value_form.is_valid():
            new = value_form.save(commit=False)
            prediction = Cal_numirology(new)
            prediction.channels()
            prediction.soul_lessons()
            prediction.birth_canal()
            prediction.final_value()
            new.personal_predictions = prediction.purpose_personal
            new.social_predictions = prediction.social_purpose
            new.spiritual_predictions = prediction.spiritual_purpose
            new.save()
            return redirect('paymate:list')
    else:
        value_form = UsetForm()
    return render(request, 'paymate/create.html', {'value_form': value_form})

