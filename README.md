# SPEECH-RECOGNITION-SYSTEM

COMPANY: CODTECH IT SOLLUTIONS

NAME: Venna Leelavathi

INTERN ID: CT06DF1809

DOMAIN: ARTIFICIAL INTELLIGENCE

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION: This program demonstrates how to build a basic Speech-to-Text system in Python using two popular approaches: one with the speech_recognition library and another with Facebook’s Wav2Vec2, a deep learning model accessed via Hugging Face’s transformers library. The purpose of this system is to convert spoken language into written text by leveraging powerful pre-trained models.
The first method uses the Python library speech_recognition, which provides a simple interface to various speech recognition engines, including the Google Web Speech API. This part of the program allows the user to speak into a microphone. The system records the speech, processes it, and sends it to Google's online API, which returns the transcribed text.
The second method involves using Wav2Vec2, a state-of-the-art, transformer-based model for automatic speech recognition (ASR), trained on large English datasets. It works entirely offline, making it ideal for privacy-conscious applications or environments with limited internet access.

The process involves several steps:

A .wav audio file is loaded using the torchaudio library.

The audio is resampled to 16 kHz if necessary, ensuring compatibility with the model.

The raw audio waveform is tokenized using a pre-trained tokenizer from Hugging Face.

The tokenized input is passed through the Wav2Vec2 model to obtain predictions.

The predictions are decoded into human-readable text using the model’s decoder.

This method offers high accuracy, especially in clean audio environments, and supports customization for different languages and accents with fine-tuning. It is suitable for building more advanced, production-ready speech recognition systems.
Comparison and Use Cases:
Both methods serve different purposes. The speech_recognition approach is best for beginners, quick demos, or low-stakes applications that can rely on cloud services. Wav2Vec2, on the other hand, is better suited for offline, accurate, and scalable systems that can run independently of internet access.

By combining modern tools and models, this program demonstrates the power and flexibility of building speech-enabled applications. Whether you're working on accessibility tools, voice assistants, or automated transcription services, these methods provide a strong foundation for creating efficient and intelligent Speech-to-Text solutions.

INPUT:

[with_speech.docx](https://github.com/user-attachments/files/21074715/with_speech.docx)

OUTPUT:

Hello, I am completing my internship task using AI.
