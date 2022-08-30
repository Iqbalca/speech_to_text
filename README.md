# Speech to Text Recognition

## This repository uses the huggingface and the transformers library

- The huggingface library is the most popular NLP library with over 68,000 stars on [github](https://github.com/huggingface/transformers)
- It provides state-of-the-art natural processing models and very clean API.
  
- Transformers library supports with a deep learning library like PyTorch, TensorFlow

- It supports Python 3.6+, PyTorch 1.1.0+, TensorFlow 2.0+, and Flax
  
- It can be used to perform Speech to Text Conversion in German Language

## Facebook wav2vec2 large xlsr-53-German 

The model facebook wav2vec2 large xlsr-53-german is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language.

- It is multilingual pre-trained wav2vec 2.0 (XLSR)
- Architecture is based on Transformers’ encoder
- Datasets on which a pre-trained model was trained (Multilingual LibriSpeech, Common Voice, Babel)

## Model usage

- We can find this model easily in transformers python library.
- To download and use any of the pretrained models for our given task
- We  just need to use few lines of codes (PyTorch version). 


Here  is an example to download using pip (a package installer for Python)
  

> Download and install using pip
> 
>> pip install transformers
>

### Usage in Python


```````

# Import model and tokenizer
from transformers import AutoModel, AutoTokenizer 

# Define the model repo
model_name = "facebook/wav2vec2-large-xlsr-53-german" 


# Download pytorch model
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Transform input tokens 
inputs = tokenizer("Hello world!", return_tensors="pt")

# Model apply
outputs = model(**inputs)

````````

Code can be found under the repo *speech_to_text/test/*

Link to the [model](https://huggingface.co/facebook/wav2vec2-large-xlsr-53-german)can be found [here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/wav2vec2)




We have also used  a fine tuned version of this model with

- German dataset: Common Voice (Version 6.1)

Common voice is a crowd-sourced read speech corpus and may have noisy dialogues.

Link to the [model](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-german) can be found [here](https://github.com/jonatasgrosman/wav2vec2-sprint)
