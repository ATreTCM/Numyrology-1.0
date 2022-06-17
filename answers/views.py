from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Social_predictions, Spiritual_predictions, Personal_predictions, Comments, Services
from .forms import Pay_nailsForm
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