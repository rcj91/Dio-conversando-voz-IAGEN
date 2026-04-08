import os
from gtts import gTTS


def text_to_speech(
    text: str,
    language: str = "pt",
    file_path: str = "data/output/response_audio.mp3"
) -> str:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(file_path)

    return os.path.abspath(file_path)