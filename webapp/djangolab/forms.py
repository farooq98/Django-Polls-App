from django import forms
from .models import Options

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['question', 'choice_text', 'votes']

        widgets = {
            'question' : forms.Select(attrs={'class':'form-control'}),
            'choice_text' : forms.TextInput(attrs={'class':'form-control'}),
            'vote' : forms.TextInput(attrs={'class':'form-control'}),
        }
class VoteForm(forms.Form):
    pass

