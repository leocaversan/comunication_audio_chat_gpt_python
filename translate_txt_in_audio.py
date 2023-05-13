from gtts import gTTS
from IPython.display import Audio, HTML


def translate_txt_audio(response_gpt):
    
    gtts_object = gTTS(text=response_gpt, lang='pt')
    response_audio = 'content/response_audio.wav'
    gtts_object.save(response_audio)
    # Audio(response_audio, autoplay=True)

translate_txt_audio("hora de acordar meu anjo, acorda Ruby")