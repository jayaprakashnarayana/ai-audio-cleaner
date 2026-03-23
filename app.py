import gradio as gr
import noisereduce as nr
import scipy.io.wavfile as wavfile
import librosa
import numpy as np
import os

def clean_audio(audio_path):
    if audio_path is None:
        return None
    
    try:
        # Load audio file using librosa (handles various formats like mp3, wav, etc.)
        y, sr = librosa.load(audio_path, sr=None)
        
        # Perform noise reduction
        # This uses the default stationary noise reduction approach
        reduced_noise = nr.reduce_noise(y=y, sr=sr)
        
        # Save the cleaned audio to a temporary wav file
        output_path = "cleaned_audio.wav"
        wavfile.write(output_path, sr, reduced_noise.astype(np.float32))
        
        return output_path
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None

# Create Gradio interface
interface = gr.Interface(
    fn=clean_audio,
    inputs=gr.Audio(type="filepath", label="Upload Noisy Audio"),
    outputs=gr.Audio(type="filepath", label="Clean Audio Output"),
    title="AI Audio Noise Cleaner",
    description="Upload a noisy audio file and get a clean, noiseless version back. Processing happens locally on your Mac.",
    flagging_mode="never"
)

if __name__ == "__main__":
    print("Starting the Audio Cleaner App on http://127.0.0.1:7860")
    interface.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
