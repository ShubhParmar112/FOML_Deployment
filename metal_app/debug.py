# metal_app/debug.py
import numpy as np
import librosa
from tensorflow.keras.models import load_model
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'metal_app', 'metal_prediction_MyData.h5')
model = load_model(MODEL_PATH)

def test_with_sample_audio():
    # Generate 1024 samples of silence
    silence = np.zeros(1024, dtype=np.float32)
    silence = silence.reshape(1, 1024, 1)
    pred = model.predict(silence, verbose=0)
    print("Silence →", pred)

    # Generate noise (like metal tap)
    noise = np.random.uniform(-0.5, 0.5, 1024).astype(np.float32)
    noise = noise.reshape(1, 1024, 1)
    pred = model.predict(noise, verbose=0)
    print("Noise →", pred)