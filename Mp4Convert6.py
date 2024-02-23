import speech_recognition as sr
import ffmpeg
from openai import OpenAI
client = OpenAI(api_key='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')

def transcribe_video_audio_to_text(video_file):
    audio_file = "C:\\Hacked_Jan6\\Metamorphosis\\temp_audio6.wav"
    (
    ffmpeg
    .input(video_file)
    .output(audio_file, format='wav')
    .run()
    )

    audio_file = open(audio_file, "rb")

    try:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text",
            prompt="include filler words",
        )
        return ("".join(transcript.split(',')))
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    video_file = "C:\Hacked_Jan6\Metamorphosis\AnswerRecording6.mp4"
    text_file = "C:\\Hacked_Jan6\\Metamorphosis\\transcribed_text6.txt"

    transcribed_text = transcribe_video_audio_to_text(video_file)

    with open(text_file, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(transcribed_text)

    print("Transcription complete. Text saved to", text_file)

main()
