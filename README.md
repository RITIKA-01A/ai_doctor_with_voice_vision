# 🧠👨‍⚕️ AI Doctor with Vision and Voice

An interactive AI-powered doctor assistant that uses multimodal capabilities (image + audio input) to analyze patient symptoms and respond with medically-informed advice.

---

## 🚀 Features

- 🧠 **Multimodal Brain**: Uses a powerful LLM (via Groq API) to understand text, image, and voice.
- 🗣️ **Patient Voice Input**: Records audio from the user and converts it to text (Speech-to-Text).
- 📷 **Image Input**: Accepts skin/visible symptom images for visual diagnosis.
- 🧑‍⚕️ **Doctor’s Voice Output**: Converts LLM response into speech using TTS.
- 🌐 **User Interface**: Built with Gradio for a clean and intuitive experience.

---

## 🧩 Project Phases

### ✅ Phase 1 – Setup the Brain of the Doctor (Multimodal LLM)
- Setup GROQ API Key
- Convert uploaded image to appropriate format
- Initialize the multimodal LLM

### ✅ Phase 2 – Setup Voice of the Patient
- Record audio using `ffmpeg` and `pyaudio`/`portaudio`
- Transcribe using STT (Speech-to-Text) model like OpenAI Whisper 

### ✅ Phase 3 – Setup Voice of the Doctor
- Convert LLM text output to speech using TTS (e.g. `gTTS` or ElevenLabs)
- Play generated voice back to the user

### ✅ Phase 4 – Setup UI for the VoiceBot
- Gradio UI to support:
  - Image upload
  - Audio recording
  - Text display for transcription & response
  - Audio playback for response

---

## 🛠️ Tech Stack

| Area              | Tools / Libraries                      |
|-------------------|----------------------------------------|
| Language Model    | Groq (LLM API)                         |
| Speech-to-Text    | Whisper / SpeechRecognition |
| Audio Recording   | ffmpeg, portaudio, sounddevice         |
| Text-to-Speech    | gTTS / ElevenLabs                      |
|                        |
| UI                | Gradio                                 |
| Language          | Python                                 |

---

## 💾 Installation

```bash
git clone https://github.com/RITIKA-01A/ai-doctor-vision-voice.git
cd ai-doctor-vision-voice
pip install -r requirements.txt
```

## 🙋‍♀️ Author
Ritika Kumari

## ▶️ Run the App
```
python gradio.py
```
