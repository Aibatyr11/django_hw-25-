from cProfile import label

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, modelform_factory, DecimalField
from django.forms.widgets import Select

from bboard.models import Bb, Rubric, IceCream


# BbForm = modelform_factory(
#     Bb,
#     fields=('title', 'content', 'price', 'rubric'),
#     labels={'title': 'Название товара'},
#     help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#     field_classes={'price': DecimalField},
#     widgets={'rubric': Select(attrs={'size': 8})}
# )


# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'}
#         help_texts = {'rubric': 'Не забудьте выбрать рубрику!'}
#         field_classes = {'price': DecimalField}
#         widgets = {'rubric': Select(attrs={'size': 8})}


# class BbForm(ModelForm):
#     title = forms.CharField(label='Название товара')
#     content = forms.CharField(label='Описание',
#                               widget=forms.widgets.Textarea())
#     price = forms.DecimalField(label='Цена', decimal_places=2)
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
#                                     label='Рубрика',
#                                     help_text='Не забудьте выбрать рубрику!',
#                                     widget=forms.widgets.Select(attrs={'size': 8}))
#
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#
#
# class RegisterUserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Пароль')
#     password2 = forms.CharField(label='Пароль (повторно)')
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2',
#                   'first_name', 'last_name')



#hw1
class BbForm(ModelForm):
    title = forms.CharField(label='Название товара')
    price = forms.DecimalField(label='Цена', decimal_places=2)


    class Meta:
        model = Bb
        fields = ('title', 'price')

#hw2

class IceCreamForm(ModelForm):
    name = forms.CharField(label='Название icecream')
    price = forms.IntegerField(label='цена')
    class Meta:
        model = IceCream
        fields = ('name', 'price')


