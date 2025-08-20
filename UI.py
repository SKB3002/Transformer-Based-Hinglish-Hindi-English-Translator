import gradio as gr
from pipeline import hinglish_to_english

def interface_fn(hinglish_text):
    hindi, english = hinglish_to_english(hinglish_text)
    return hindi, english

demo = gr.Interface(
    fn=interface_fn,
    inputs=gr.Textbox(lines=2, placeholder="Enter Hinglish text here..."),
    outputs=[gr.Textbox(label="Hindi (Devanagari)"), gr.Textbox(label="English")],
    title="Hinglish → Hindi → English Translator",
    description="Step 1: Hinglish text → Hindi (Devanagari). Step 2: Hindi → English."
)

if __name__ == "__main__":
    demo.launch()
