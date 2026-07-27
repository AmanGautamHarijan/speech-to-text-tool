import os
import speech_recognition as sr

OUTPUT_FILE = "transcription.txt"


def transcribe_audio(file_path):
    """Transcribe a wav file to text using Google's speech API."""
    r = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print("Reading audio file...")
            audio = r.record(source)  # load the whole file into memory

        print("Transcribing... this can take a few seconds")
        text = r.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Couldn't understand the audio - try a clearer recording")
    except sr.RequestError as e:
        print(f"API request failed: {e}")
    except Exception as e:
        # catch-all so a weird file doesn't just crash the script
        print(f"Something went wrong: {e}")

    return None


def save_transcription(text, output_file=OUTPUT_FILE):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved to {output_file}")


def main():
    print("=== Speech-to-Text Transcription Tool ===\n")

    file_path = input("Path to your .wav file: ").strip()

    if not os.path.isfile(file_path):
        print(f"Can't find '{file_path}' - check the path and try again")
        return

    if not file_path.lower().endswith(".wav"):
        print("Heads up: this works best with .wav files, but trying anyway...")

    text = transcribe_audio(file_path)

    if not text:
        print("Transcription failed, nothing saved.")
        return

    print("\n--- Transcribed Text ---")
    print(text)
    print("------------------------\n")

    save_transcription(text)


if __name__ == "__main__":
    main()
