import speech_recognition as sr
import soundfile

def created_new_audio(audio_path):
    data, samplerate = soundfile.read(audio_path)
    soundfile.write(audio_path, data, samplerate, subtype='PCM_16')

def translate_audio_in_text(file_name):
    created_new_audio(file_name)
    r = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='pt-BR')
    return text 