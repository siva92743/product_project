from django import forms

from app.models import Equipments, Category, Sales, Customer


class Task(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'


class Item(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class Sell(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'


class User(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'