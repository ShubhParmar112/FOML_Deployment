# metal_app/views.py
from django.shortcuts import render
from django.conf import settings
from .forms import AudioUploadForm
from .audio_processor import predict_metal_from_file
import os

def home(request):
    form = AudioUploadForm()
    result = None

    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']
            file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', 'temp_recording.wav')

            # Ensure directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Save uploaded file
            with open(file_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Predict
            result = predict_metal_from_file(file_path)

            # Clean up temp file
            if os.path.exists(file_path):
                os.remove(file_path)

    return render(request, 'index.html', {
        'form': form,
        'result': result
    })