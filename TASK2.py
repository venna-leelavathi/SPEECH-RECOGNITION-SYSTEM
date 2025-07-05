import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa

# Load pre-trained Wav2Vec2 model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Load and process audio
def load_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    if sample_rate != 16000:
        waveform = librosa.resample(waveform.numpy()[0], orig_sr=sample_rate, target_sr=16000)
        waveform = torch.tensor([waveform])
    return waveform

# Transcribe
def transcribe(audio_path):
    audio_input = load_audio(audio_path)
    input_values = tokenizer(audio_input.squeeze().numpy(), return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    return transcription.lower()

# Example usage
print("Transcription:", transcribe("your_audio.wav"))
