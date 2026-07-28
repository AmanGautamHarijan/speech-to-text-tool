import speech_recognition as sr

OUTPUT_FILE = "transcription.txt"


def record_from_microphone():
    """Listen on the default mic and return the recorded audio."""
    r = sr.Recognizer()

    try:
        with sr.Microphone(device_index=8) as source:  # Headset (Nirvana Ion ANC) - confirmed working
            print("Adjusting for background noise, hang on...")
            r.adjust_for_ambient_noise(source, duration=2)
            print(f"Energy threshold set to: {r.energy_threshold:.0f}")

            # Bluetooth mics often have a noisy baseline that throws off
            # auto-adjustment - give it more room and don't let it keep
            # re-adjusting mid-recording.
            r.dynamic_energy_threshold = False
            r.pause_threshold = 1.0

            print("Listening... speak now!")
            # timeout = max seconds to wait for speech to start
            # phrase_time_limit = max seconds to record once speech starts
            audio = r.listen(source, timeout=8, phrase_time_limit=15)
            print("Got it.")
            return audio

    except sr.WaitTimeoutError:
        print("Didn't hear anything - check your mic and try again")
        return None
    except OSError:
        print("No microphone found - check your audio input device")
        return None


def transcribe(audio):
    r = sr.Recognizer()

    # Save what was actually recorded so we can listen back and debug
    # if transcription keeps failing.
    with open("debug_recording.wav", "wb") as f:
        f.write(audio.get_wav_data())
    print("Saved raw recording to debug_recording.wav - play it to check audio quality")

    try:
        print("Transcribing...")
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't make out what was said")
    except sr.RequestError as e:
        print(f"API request failed: {e}")

    return None


def save_transcription(text, output_file=OUTPUT_FILE):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved to {output_file}")


def main():
    print("=== Speech-to-Text Transcription Tool (Microphone) ===\n")
    input("Press Enter when you're ready to record...")

    audio = record_from_microphone()
    if audio is None:
        return

    text = transcribe(audio)
    if not text:
        print("Transcription failed, nothing saved.")
        return

    print("\n--- Transcribed Text ---")
    print(text)
    print("------------------------\n")

    save_transcription(text)


if __name__ == "__main__":
    main()