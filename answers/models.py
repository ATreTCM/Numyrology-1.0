
from django.db import models
from django.urls import reverse


class Social_predictions(models.Model):
    
    """Социальное предназначение и описание"""
    social_purpose = models.DecimalField(
        max_digits=100, 
        decimal_places=2, 
        default=0,
        verbose_name='Социальное предназначение'
        )
    
    header = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
        )
    
    predictions_social = models.TextField(
        max_length=3000, 
        verbose_name='Социальное предназначение текст'
        )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Социальное предназначение'
        verbose_name_plural = 'Социальные предназначения'


class Spiritual_predictions(models.Model):
    """Духовное предназначение и описание"""
    
    spiritual_purpose = models.DecimalField(
        max_digits=100, 
        decimal_places=2, 
        default=0,
        verbose_name='Духовное предназначение'
        )
    
    header = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
        )
    
    predictions_spiritual = models.TextField(
        max_length=3000, 
        verbose_name='Духовное предназначение текст'
        )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Духовное предназначение'
        verbose_name_plural = 'Духовные предназначения'


class Personal_predictions(models.Model):
    """Личное предназначение и описание"""
    
    purpose_personal = models.DecimalField(
        max_digits=100, 
        decimal_places=2, 
        default=0,
        verbose_name='Личное предназначение'
        )
    
    header = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
        )
    
    predictions_personal = models.TextField(
        max_length=3000, 
        verbose_name='Личное предназначение текст'
        )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Личное предназначение'
        verbose_name_plural = 'Личные предназначения'


class Comment(models.Model):
    """Отзывы на услуги"""
    
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
        )
    
    comment = models.TextField(
        max_length=1000, 
        verbose_name='Отзыв'
        )
    
    avka = models.ImageField(
        blank=True, 
        null=True, 
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='Фото'
        )
    
    date_add = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('answers:comment', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date_add']


class Service(models.Model):
    """Услуги и цены"""
    
    header = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
        )
    
    text = models.TextField(
        max_length=1000,
        verbose_name='Услуги'
        )
    
    like_view = models.CharField(
        max_length=100,
        verbose_name='как выглядит',
        default=" "
        )
    
    price = models.DecimalField(
        max_digits=100, 
        decimal_places=2,
        default=0, 
        verbose_name='Цена услуги'
        )

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('answers:service', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Uset(models.Model):
    """Таблица пользователя"""
    
    name = models.CharField(
        max_length=50, 
        verbose_name='Имя',
        default='someuser'
        )
    
    born_date = models.CharField(
        max_length=20,
        verbose_name='Дата рождения'
        )
    
    social_predictions = models.DecimalField(
        max_digits=50,
        decimal_places=0,
        default=0,
        verbose_name='Социальное предназначение'
        )
    
    spiritual_predictions = models.DecimalField(
        max_digits=50, 
        decimal_places=0, 
        default=0,
        verbose_name='Духовное предназначение'
        )
    
    personal_predictions = models.DecimalField(
        max_digits=50, 
        decimal_places=0, 
        default=0,
        verbose_name='Личное предназначение'
        )
    
    date_add = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Калькулятор пользователя'
        verbose_name_plural = 'Калькуляторы пользователей'
