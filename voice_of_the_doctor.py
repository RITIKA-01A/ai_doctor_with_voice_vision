## Step1a : Setup text to speech ttsmodel gTTs
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="hi"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="mera naam ritika hai "
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


## Step1b : Setup text to speech ttsmodel ElevenLabs
import os
from elevenlabs.client import ElevenLabs

# Provide your API key directly or via environment
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY") or "your-actual-api-key-here"

def get_voice_id_by_name(client, name="Aria"):
    voices = client.voices.get_all()
    for voice in voices.voices:
        if voice.name.lower() == name.lower():
            return voice.voice_id
    raise ValueError(f"Voice '{name}' not found.")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # Dynamically get the voice_id for "Aria"
    voice_id = get_voice_id_by_name(client, name="Aria")

    # Generate and save the audio
    audio_chunks = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice_id,
        model_id="eleven_turbo_v2_5",
        output_format="mp3_22050_32"
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio_chunks:
            if chunk:
                f.write(chunk)

    print(f" Audio saved to {output_filepath}")


# # Example usage
# text_to_speech_with_elevenlabs(
#     input_text="Hello! I am your AI doctor speaking from ElevenLabs.",
#     output_filepath="elevenlabs_test.mp3"
# )







## Step2:Use model for test output to voice


import subprocess
import platform
from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Generate MP3 from text
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Convert mp3 to wav for SoundPlayer
            wav_path = output_filepath.replace(".mp3", ".wav")
            sound = AudioSegment.from_mp3(output_filepath)
            sound.export(wav_path, format="wav")
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


