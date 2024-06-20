from django import forms

# class ImageGenerationForm(forms.Form):
#     prompt = forms.CharField(label='Prompt', max_length=255)

class StoryForm(forms.Form):
    family_member_name = forms.CharField(label='Family Member Name', max_length=100)
    relation = forms.CharField(label='Relation to Main Character', max_length=100)
    year = forms.IntegerField(label='Year of the Picture')
    description = forms.CharField(label='Description of the Story', widget=forms.Textarea)
