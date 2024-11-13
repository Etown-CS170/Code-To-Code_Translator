import gradio as gr
import anthropic
from anthropicKey import key

client = anthropic.Anthropic(
    api_key=key,
)

def get_response(request):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="Translate the given code into Java code.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": request
                    }
                ]
            }
        ]
    )
    return message.content

demo = gr.Interface(fn=get_response, inputs="text", outputs="text")
    
demo.launch(share=True) 