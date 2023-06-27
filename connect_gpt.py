import openai
from dotenv import load_dotenv

load_dotenv()
def interaction_chatgpt(transcription):
    print(transcription)
    openai.api_key = os.getenv('KEY_CHATGPT')

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[{
            "role":"user", "content": transcription
        }]
    )
    chatgpt_response = response.choices[0].message.content
    return chatgpt_response

