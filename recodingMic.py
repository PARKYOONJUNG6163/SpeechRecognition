# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()


file_name = str(input("What is your Name?"))
count = 1

for i in range(10) : # 10번 반복
    with sr.Microphone() as source:
        print("Say Bed-Bird-Cat-Dog-Down !")
        audio = r.listen(source)

    result_name = file_name + "_" + str(count)
    print(result_name)
    # write audio to a WAV file
    with open(result_name+".wav", "wb") as f:
        f.write(audio.get_wav_data())
        print(result_name + " : Finish !")

    count += 1
