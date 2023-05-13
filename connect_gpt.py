import openai

def interaction_chatgpt(transcription):
    print(transcription)
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[{
            "role":"user", "content": transcription
        }]
    )
    chatgpt_response = response.choices[0].message.content
    return chatgpt_response

