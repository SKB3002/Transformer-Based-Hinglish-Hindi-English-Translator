from datasets import Dataset, DatasetDict

dataset = Dataset.from_dict({
    "src": clean_hindi,
    "tgt": clean_english
})

# Split into train/validation (90/10 split)
dataset = dataset.train_test_split(test_size=0.1, seed=42)
dataset = DatasetDict({
    "train": dataset['train'],
    "validation": dataset['test']
})

print(dataset)


# Load Model and Tokenizer

from transformers import MarianTokenizer

MODEL_NAME = "Helsinki-NLP/opus-mt-hi-en"
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)

# Preprocess 

def preprocess(batch):
    model_inputs = tokenizer(batch['src'], truncation=True, padding='max_length', max_length=40)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(batch['tgt'], truncation=True, padding='max_length', max_length=40)
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

tokenized_ds = dataset.map(preprocess, batched=True)
tokenized_ds = tokenized_ds.remove_columns(['src','tgt'])
tokenized_ds.set_format('torch')

# Training Arguments

from transformers import Seq2SeqTrainingArguments, 

training_args = Seq2SeqTrainingArguments(
    output_dir="./mt_model",
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    save_total_limit=2,
    num_train_epochs=3,
    predict_with_generate=True,
    logging_dir="./logs",
    logging_steps=50,
    fp16=True
)

# Trainer 
from transformers import Seq2SeqTrainer, DataCollatorForSeq2Seq

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds[train'],
    eval_dataset=tokenized_ds['validation'],
    processing_class=tokenizer2,
    data_collator=data_collator
)


trainer.train()
