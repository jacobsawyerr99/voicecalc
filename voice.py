import speech_recognition as speechrecog

from operations import calculate

print("your speech recog version is" + speechrecog.__version__)


recognizer = speechrecog.Recognizer()

# mic_index and def_mic are used to get default microphones from system. This is
# typically done through microphone "default". creates a list and identifies the default input
mic_indices= speechrecog.Microphone.list_microphone_names()
def_mic_index = mic_indices.index("default")

# setting variable of index for input device. works on my system (fedora). will need to 
# test other operating systems and linux distros.
my_mic = speechrecog.Microphone(device_index=def_mic_index)


# getting input from user
with my_mic as src:
    print("Say desired problem.")
    recognizer.adjust_for_ambient_noise(src)
    aud =  recognizer.listen(src)
voice_input = recognizer.recognize_google(aud)


print(voice_input)

calculate(voice_input)





