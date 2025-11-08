# metal_app/debug_real.py
import numpy as np
import librosa
from metal_app.audio_processor import predict_metal_from_file
import soundfile as sf
import tempfile
import os

def debug_with_real_audio():
    # Create 1-second silence
    sr = 16000
    silence = np.zeros(sr, dtype=np.float32)
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, silence, sr)
        path = f.name

    print("Testing SILENCE:")
    result = predict_metal_from_file(path)
    print(result)

    os.unlink(path)

    # Create loud metal-like hit
    hit = np.zeros(sr)
    hit[8000:8100] = np.hanning(100) * 0.9
    hit += np.random.normal(0, 0.02, sr)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, hit, sr)
        path = f.name

    print("\nTesting LOUD HIT:")
    result = predict_metal_from_file(path)
    print(result)

    os.unlink(path)

if __name__ == "__main__":
    debug_with_real_audio()