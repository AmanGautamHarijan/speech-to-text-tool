# Speech-to-Text Transcription Tool

Small Python script that turns spoken audio into text, using the
`SpeechRecognition` library + Google's free speech API.

## Files

- `speech_to_text.py` - transcribes a `.wav` file
- `speech_to_text_microphone.py` - same thing but records from your mic instead
- `requirements.txt` - deps

## Setup

Python 3.7+ required.

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### PyAudio being annoying?

`PyAudio` (only needed for the mic version) can be a pain to install since it
depends on PortAudio. If `pip install` fails on it:

- **Windows:** `pip install pipwin && pipwin install pyaudio`
- **Mac:** `brew install portaudio` then `pip install pyaudio`
- **Linux:** `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

If you just want to transcribe files (not use the mic), you can ignore this
entirely - `speech_to_text.py` doesn't need PyAudio.

## Usage

**Transcribe a file:**

```bash
python speech_to_text.py
```

It'll ask for a file path:

```
Path to your .wav file: sample.wav
```

Prints the result and saves it to `transcription.txt`.

**Transcribe from mic (optional):**

```bash
python speech_to_text_microphone.py
```

Hit Enter, talk, wait. Same output as above.

## How it works

1. `sr.Recognizer()` does the actual work
2. Audio comes in either from a file (`sr.AudioFile`) or the mic (`sr.Microphone`)
3. Gets converted to `AudioData`
4. `recognize_google()` sends it off to Google and gets text back
5. Errors are handled so it doesn't just crash:
   - `UnknownValueError` - audio wasn't clear enough to understand
   - `RequestError` - couldn't reach the API (probably no internet)

## Notes

- Needs an internet connection since it hits Google's API
- `recognize_google()` is the free/keyless tier - fine for testing, but for
  anything serious you'd want Google Cloud Speech-to-Text with a proper API key
- Works best with clear audio, not a lot of background noise