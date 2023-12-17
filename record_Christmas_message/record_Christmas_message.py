

import sounddevice as sd
from scipy.io.wavfile import write
import wavio

def record_voice(filename, duration, fs=44100):
    """
    Record voice and save to a file.
    
    Args:
    - filename: The name of the file where the recording will be saved.
    - duration: The recording duration in seconds.
    - fs: The sampling frequency. Default is 44100 Hz.
    """
    print("Recording...")

    # Record audio for the given number of seconds
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished

    print("Recording finished. Saving the file...")

    # Save the recording as a WAV file
    wavio.write(filename, recording, fs, sampwidth=2)

    print(f"File saved as {filename}")

# Example usage
record_voice("my_voice_recording.wav", 5)  # Record for 5 seconds
