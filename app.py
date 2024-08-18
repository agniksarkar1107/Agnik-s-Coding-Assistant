import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}



def generate_response(prompt):
    

    data={
        "model":"codify",
        "prompt":prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Coding Question"),
    outputs="text",
    title="🛠️ CODIFY",
    description="Welcome to the Code Assistant! Ask me anything about programming, and I'll do my best to help you. 💻✨",
    theme="default",
)

interface.css = """
    #component-0 {
        background-color: #1f2937;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    #component-1 {
        background-color: #374151;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    .title {
        font-family: 'Arial', sans-serif;
        color: #f9fafb;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .description {
        font-family: 'Arial', sans-serif;
        color: #e5e7eb;
        font-size: 16px;
    }
"""

interface.launch(share=True)
