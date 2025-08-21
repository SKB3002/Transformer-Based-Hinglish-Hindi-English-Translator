# **Transformer-Based-Hinglish-Hindi-English-Translator**


Fine-tuning Transformers for Multilingual Translation
This project demonstrates a complete NLP pipeline for translating Hinglish (Hindi + English mix) text into English, passing through an intermediate Hindi translation step.

Deployed on Hugging Face Spaces, this model is accessible for both technical users (via API) and non-technical users (via Web UI).

## ✨ Features

🔀 **Transliteration with IndicTrans:**
 – converts Hinglish (romanized Hindi) into proper Devanagari Hindi.

🤖 **Fine-Tuned Transformer (mBART/MarianMT)** – trained for Hinglish → Hindi translation.

🌍 **Two-Stage Pipeline** – Hinglish → Hindi → English for cleaner, context-aware translations.

☁️ **Deployment** – Hosted on Hugging Face with public inference API.
(https://huggingface.co/spaces/SKB3002/Transformer-Based-Hinglish-Hindi-English-Translator)

---

## 📂 Project Structure

├── app.py                # Main inference script

├── pipeline.py           # Full translation pipeline (Hinglish → Hindi → English)

├── config.json           # Model config for Hugging Face deployment

├── requirements.txt      # Dependencies

└── README.md             # Project Documentation

---

### 🚀 Pipeline Workflow

**Input (Hinglish):**
"kal raat party mast thi bro"

**Step 1** (Transliteration → Hindi):
"कल रात पार्टी मस्त थी ब्रो"

**Step 2** (Translation → English):
"Last night’s party was awesome bro"
 

--- 

## 📊 Training & Fine-Tuning

**Base Model:** MarianMT

**Dataset:**  Hindi-English parallel corpora by IIT Bombay

**Fine-Tuning:** Hugging Face Transformers (Trainer API)

**Evaluation Metric:** BLEU, SacreBLEU

---

## 🌟 Future Improvements

🔬 Train on larger Hinglish-English corpora

🧠 Add *context-aware translation* with **RAG** or **LLMs**

📱 Deploy as a mobile/web app for real-world use

---

## 📜 License

**MIT License**



## 🙌 Acknowledgements

Hugging Face Transformers - (https://huggingface.co/Helsinki-NLP/opus-mt-hi-en)

IndicTrans Transliteration - (https://github.com/libindic/indic-trans)

🔥 Check out the live model here → [Hugging Face Deployment](https://huggingface.co/spaces/SKB3002/Transformer-Based-Hinglish-Hindi-English-Translator)

