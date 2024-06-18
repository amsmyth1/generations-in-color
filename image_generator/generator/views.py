from django.shortcuts import render
from django.conf import settings
import openai
from .forms import ImageGenerationForm
from dotenv import load_dotenv

openai.api_key = settings.OPENAI_API_KEY

def generate_image(request):
    if request.method == 'POST':
        form = ImageGenerationForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            response = openai.images.generate(
                model="dall-e-3",
                prompt="a white siamese cat",
                size="1024x1024",
                quality="standard",
                n=1,
                )
            image_url = response.data[0].url
            return render(request, 'generator/result.html', {'image_url': image_url})
    else:
        form = ImageGenerationForm()
    return render(request, 'generator/form.html', {'form': form})
