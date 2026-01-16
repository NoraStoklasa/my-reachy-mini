import sounddevice as sd
import soundfile as sf
import tempfile
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def speak(text, voice="alloy"):
    # Create temporary audio file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        audio_path = f.name

    # Generate speech
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
    ) as response:
        response.stream_to_file(audio_path)

    # Play audio
    data, samplerate = sf.read(audio_path)
    sd.play(data, samplerate)
    sd.wait()
