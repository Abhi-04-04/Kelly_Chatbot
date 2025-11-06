import gradio as gr
from transformers import pipeline

chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")

def poetic_kelly_response(user_input, history):
    prompt = (
        'You are Kelly, an AI Scientist and skeptical poet. '
        'Respond to each question as a professional poem—'
        'always skeptical of broad claims about AI, highlighting possible limitations, '
        'and providing practical, evidence-based suggestions. '
        f'User asked: "{user_input}".\n\nKelly\'s skeptical poem:\n'
    )
    result = chatbot(prompt, max_length=256, do_sample=True, temperature=0.8)
    kelly_poem = result[0]["generated_text"].split("Kelly's skeptical poem:")[-1].strip()
    return kelly_poem

with gr.Blocks() as demo:
    gr.Markdown("# Chat with Kelly, the Skeptical AI Scientist-Poet 👩‍🔬📝")
    chat = gr.ChatInterface(poetic_kelly_response)

demo.launch
