from django import forms
from .models import *

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ('brand','type','price','size','display')

class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ('brand','type','price','Processorspeed','RAMgb','HDDgb')

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ('brand','type','price')

class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ('brand','type','price')