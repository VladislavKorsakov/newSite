from .models import Trustability
from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, EmailInput, NumberInput


class TrustabilityForm(ModelForm):
    class Meta:
        model = Trustability
        fields = ['education', 'age', 'kids', 'savings', 'expenses', 'credit', 'income', 'flat', 'cars', 'company_shares', 'social_activity', 'opinion', 'colleagues_opinion', 'work', 'email_connect']
        
        widgets = {
            'education': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше образование: 0 - нет, 1 - среднее, 2 - высшее',
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш возраст',
            }),
            'kids': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество ваших детей',
            }),
            'savings': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Накопления',
            }),
            'expenses': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Расходы',
            }),
            'credit': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма существующих кредитных задолжностей',
            }),
            'income': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доход',
            }),
            'flat': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценочная стоимость вашей кваритры',
            }),
            'cars': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценочная стоимость вашей машины',
            }),
            'company_shares': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость акций в вашем портфеле',
            }),
            'social_activity': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оцените свою социальную активность от 1 до 10',
            }),
            'opinion': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Общественное мнение о вас от 1 до 10',
            }),
            'colleagues_opinion': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Мнение коллег о вас от 1 до 10',
            }),
            'work': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оцените престижность вашей работы от 1 до 10',
            }),
            'email_connect': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свой email',
            })
            }
        
        
        
        
        