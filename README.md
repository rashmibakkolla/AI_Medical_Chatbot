
# AI Medical Chatbot 🩺👁️🎤

> **Transforming Healthcare with Intelligent Voice and Vision**
> An end‑to‑end AI Doctor Assistant that uses **speech, vision, and AI** to deliver medical advice and recommendations in a seamless and interactive way.

---

## 🎯 Project Layout

### ⚡️ **Phase 1 — Setup the Brain of the Doctor (Multimodal LLM)**

* ✅ Setup GROQ API Key
* ✅ Convert Image to Required Format
* ✅ Setup Multimodal LLM (Meta Llama 3 Vision)

### 🎤 **Phase 2 — Setup Voice of the Patient**

* ✅ Setup Audio Recorder (`ffmpeg` & `portaudio`)
* ✅ Speech‑to‑Text (STT) Model for Transcription (OpenAI Whisper)

### 🔊 **Phase 3 — Setup Voice of the Doctor**

* ✅ Text‑to‑Speech Model (gTTS) for Doctor Responses
* ✅ Model to Output Text as Speech

### 💻 **Phase 4 — Setup UI for the VoiceBot**

* ✅ Interactive VoiceBot UI with **Gradio**
* ✅ Enables Voice and Image Inputs
* ✅ Displays Text Responses and Plays Doctor's Voice Output

---

## ⚡️ Tools and Technologies

* ⚡️ **GROQ** for AI Inference
* 🗣️ **OpenAI Whisper** — Best Open Source Model for Transcription
* 👁️ **Llama 3 Vision** — Open Source Model by Meta for Image Understanding
* 🔊 **gTTS** — Text‑to‑Speech Model
* 🌐 **Gradio** — Interactive User Interface
* 🐍 **Python** — Main Programming Language
* ⚡️ **VS Code** — Development Environment

---

## 🏗️ Technical Architecture

| Phase       | Goal                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Phase 1** | ✅ User uploads an image and provides a voice query. The image and voice data are combined and passed to the Llama 3 Vision model via GROQ. |
| **Phase 2** | ✅ Transcription of user voice (using OpenAI Whisper).                                                                                      |
| **Phase 3** | ✅ Doctor’s response is generated and converted into speech using gTTS.                                                                     |
| **Phase 4** | ✅ Final output is rendered in the Gradio interface as playable audio and text response.                                                    |

![Technical Architecture Diagram](technical_architecture.png)

---

## ⚡️ Features

✅ End‑to‑End Medical Chatbot
✅ Voice‑Driven Interaction
✅ Multimodal Inputs (Voice + Images)
✅ Speech‑to‑Text, Text‑to‑Speech Integration
✅ Intelligent Medical Advice from Llama 3 Vision Model
✅ Simple and Friendly User Experience via Gradio

---

## ⚡️UI Demo
![image](https://github.com/user-attachments/assets/da8ebcae-6ad1-4bf5-b491-29cb30ed9423)


