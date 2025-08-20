from indictrans import Transliterator
import torch

# Loading transliterator (Hinglish → Hindi Devanagari)
trn = Transliterator(source='eng', target='hin')

# Loading Hindi→English model 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path_ = '/kaggle/input/hinglish-model/transformers/default/1/models/devanagri_model'

tokenizer = AutoTokenizer.from_pretrained(model_path_)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path_)

def hinglish_to_english(hinglish_text):
    # Stage 1: Hinglish → Hindi (Devanagari)
    devanagari = trn.transform(hinglish_text)
    
    # Stage 2: Hindi (Devanagari) → English
    inputs = tokenizer(devanagari, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    english = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return devanagari, english
