import whisper
from app.config.settings import WHISPER_MODEL


_model = whisper.load_model(WHISPER_MODEL)


def transcribe_audio(file_path: str, language: str = "pt") -> str:
    result = _model.transcribe(file_path, fp16=False, language=language)
    return result["text"].strip()