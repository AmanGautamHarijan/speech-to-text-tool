import speech_recognition as sr

print("Available microphones:\n")
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {name}")

print("\nIf your mic isn't device 0, note its number above.")
print("Then edit speech_to_text_microphone.py to use:")
print("    with sr.Microphone(device_index=YOUR_NUMBER) as source:")
