import importlib
import subprocess
import sys

REQUIRED_PACKAGES = {
    "openai": "openai",
    "openai-whisper": "whisper",
    "gTTS": "gtts",
    "sounddevice": "sounddevice",
    "scipy": "scipy",
    "python-dotenv": "dotenv",
}

def ensure_packages():
    missing = []

    for pip_name, import_name in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print("Instalando pacotes ausentes...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    else:
        print("Todas as dependências já estão instaladas.")

def main():
    ensure_packages()
    from app.main import main as app_main
    app_main()

if __name__ == "__main__":
    main()