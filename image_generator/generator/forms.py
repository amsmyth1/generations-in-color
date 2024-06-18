from django import forms

class ImageGenerationForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=255)
