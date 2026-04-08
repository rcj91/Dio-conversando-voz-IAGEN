from app.audio.recorder import record_audio
from app.audio.transcriber import transcribe_audio
from app.audio.tts import text_to_speech
from app.agents.culinary_agent import get_culinary_response
from app.config.settings import LANGUAGE
from app.utils.exporter import save_last_interaction_txt, append_history_txt
import os


def main():
    input_audio_path = record_audio(
        duration=6,
        file_path="data/input/request_audio.wav"
    )

    print("Áudio gravado em:", input_audio_path)

    user_text = transcribe_audio(input_audio_path, language=LANGUAGE)
    print("\nTranscrição do usuário:\n")
    print(user_text)

    response_text = get_culinary_response(user_text)
    print("\nResposta do ChefIA:\n")
    print(response_text)

    last_txt_path = save_last_interaction_txt(
        user_text=user_text,
        agent_text=response_text,
        file_path="data/output/interacao_chefia.txt"
    )

    history_txt_path = append_history_txt(
        user_text=user_text,
        agent_text=response_text,
        file_path="data/output/historico_chefia.txt"
    )

    print("\nÚltima interação salva em:", last_txt_path)
    print("Histórico salvo em:", history_txt_path)

    output_audio_path = text_to_speech(
        response_text,
        language=LANGUAGE,
        file_path="data/output/response_audio.mp3"
    )

    print("\nÁudio de resposta salvo em:", output_audio_path)
    os.startfile(output_audio_path)


if __name__ == "__main__":
    main()