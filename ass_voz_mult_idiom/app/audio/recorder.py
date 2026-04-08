import os
import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(
    duration: int = 6,
    sample_rate: int = 44100,
    file_path: str = "data/input/request_audio.wav"
) -> str:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    print(f"Ouvindo por {duration} segundos...\n")
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    write(file_path, sample_rate, audio)
    return os.path.abspath(file_path)