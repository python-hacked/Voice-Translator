from django.shortcuts import render
from .translator import recognize_speech, translate_text

def index(request):
    if request.method == 'POST':
        recognized_text = recognize_speech()
        if recognized_text:
            translated_text = translate_text(recognized_text, target_language='hi')
            return render(request, 'index.html', {'recognized_text': recognized_text, 'translated_text': translated_text})

    return render(request, 'index.html')
