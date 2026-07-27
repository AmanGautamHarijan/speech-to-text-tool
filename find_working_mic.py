import speech_recognition as sr

print("Testing all input devices for actual audio... this takes a few seconds\n")

working = sr.Microphone.list_working_microphones()

if not working:
    print("No working microphones found. This usually means a permissions")
    print("issue (check Windows mic privacy settings) rather than a code problem.")
else:
    print("Working microphones found:\n")
    for index, name in working.items():
        print(f"{index}: {name}")

    print("\nUse the FIRST one listed - update speech_to_text_microphone.py with:")
    first_index = list(working.keys())[0]
    print(f"    with sr.Microphone(device_index={first_index}) as source:")
