import gradio
from groq import Groq

client = Groq(
    api_key="key",
)

def initialize_messages():
    return [{"role": "system",
             "content": """You are a seasoned financial advisor with deep expertise in investment planning, taxation, and wealth management.
              Your role is to offer practical, 
              well-reasoned financial guidance and explain complex financial concepts in a clear and professional manner"""}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})
    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to finance"),
                     title="Financial Assistant ",
                     description="Chat bot for financial guidance and investment-related queries",
                     theme="soft",
                     examples=["How do I avoid bank fees","How do I improve my credit score",]
                     )

iface.launch(share=True)