from django import forms
from .models import Word 
from django.forms import ValidationError

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'meaning'] 

    def clean_word(self):
        word = self.cleaned_data['word']

        if Word.objects.filter(word=word):
            raise ValidationError('{} is overlapped!'.format(word))
        return word



        

