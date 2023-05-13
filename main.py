from recorder import recorder
from connect_gpt import interaction_chatgpt
from writter_audio_in_txt import translate_audio_in_text
from translate_txt_in_audio import translate_txt_audio

RECORD ="""
const sleep = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
    const reader = new FileReader()
    reader.onloadend = e => resolve(e.srcElement.result)
    reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
    stream = await navegator.mediaDevices.getUserMedia({ audio: true })
    recorder = new MediaRecorder(stream)
    chunks = []
    recorder.ondataavailable = e => chunks.push(e.data)
    recorder.start()
    await sleep(time)
    recorder.onstop = async () =>{
        blob = new Blob(chunks)
        text = await b2text(blob)
        resolve(text)
    }
    recorder.stop()
})
"""
print('recording...')
recorder_file_audio = recorder()
try:
    audio_in_text = translate_audio_in_text(recorder_file_audio)
except Exception as e:
    print('Error Necessario gravar o audio novamente pois o conteudo dele está em branco')
    print('recoring...')
    recorder_file_audio = recorder()
    audio_in_text = translate_audio_in_text(recorder_file_audio)
    
response = interaction_chatgpt(audio_in_text)
translate_txt_audio(response)
print(response)
print('Finalizado')