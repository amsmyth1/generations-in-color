from django.shortcuts import render
from django.conf import settings
import openai
from .forms import StoryForm
from dotenv import load_dotenv

openai.api_key = settings.OPENAI_API_KEY

def generate_coloring_book_prompt(family_member_name, relation, year, description):
    coloring_book_prompt = f"Generate a picture in the style of a simple clean lined coloring book. Using black lines with a white background. The photo should be in the year of {year}. Depicting {description}"
    prompt = coloring_book_prompt
    return prompt

def generate_image(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            family_member_name = form.cleaned_data['family_member_name']
            relation = form.cleaned_data['relation']
            year = form.cleaned_data['year']
            description = form.cleaned_data['description']
            prompt = generate_coloring_book_prompt(family_member_name, relation, year, description)
            print(f"*********************************************Prompt: {prompt}")
            response = openai.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
                )
            image_url = response.data[0].url
            return render(request, 'generator/result.html', {'image_url': image_url})
    else:
        form = StoryForm()
    return render(request, 'generator/form.html', {'form': form})
