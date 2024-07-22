from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class User(AbstractUser):
    name = models.CharField('Имя', max_length=50)
    psw = models.CharField('Пароль', max_length=50)
    email = models.EmailField('Email', unique=True)
    
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    
    
class Trustability(models.Model):
    
    ED_CHOICES = (
            ('0', 'Нет образования'),
            ('1', 'ПТУ'),
            ('2', 'ВЫСШЕЕ'),
        )
    
    education = models.CharField("Образование", max_length=15, choices=ED_CHOICES, null=False, default=2)
    age = models.IntegerField('Возраст', default=25, null=False)
    kids = models.IntegerField('Дети', null=False, default=0)
    
    savings = models.FloatField('Накопления', null=False, default=100000)
    expenses = models.FloatField('Расходы', null=False, default=50000)
    credit = models.FloatField('Сумма существующих кредитных задолжностей', null=False, default=0)
    income = models.FloatField('Доход', null=False, default=150000)
    
    flat = models.FloatField('Оценочная стоимость вашей кваритры', null=False, default=3000000)
    cars = models.FloatField('Оценочная стоимость вашей машины', null=False, default=2500000)
    company_shares = models.FloatField('Стоимость акций в вашем портфеле', null=False, default=500000)
    
    social_activity = models.IntegerField('Оцените свою социальную активность от 1 до 10', null=False, default=6)
    opinion = models.IntegerField('Общественное мнение о вас от 1 до 10', null=False, default=6)   
    colleagues_opinion = models.IntegerField('Мнение коллег о вас от 1 до 10', null=False, default=6)
    work = models.IntegerField('Оцените престижность вашей работы от 1 до 10', null=False, default=6)
    email_connect = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email', null=False)
    
    
    class Meta:
        verbose_name = 'Кредитоспособность'
        verbose_name_plural = 'Кредитоспособность'


    

