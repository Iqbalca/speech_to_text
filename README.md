# Speech to Text Recognition

## This repository uses the huggingface and the transformers library

- The huggingface library is the most popular NLP library with over 68,000 stars on [github](https://github.com/huggingface/transformers)
- It provides state-of-the-art natural processing models and very clean API.
  
- Transformers library supports with a deep learning library like PyTorch, TensorFlow

- It supports Python 3.6+, PyTorch 1.1.0+, TensorFlow 2.0+, and Flax
  
- It can be used to perform Speech to Text Conversion in German Language

## Selection of ASR Model

- Our research shows a selection of ASR model architectures that are pretrained on the German language and evaluates state-of-the-art open-source models in German language on diverse datasets

- With comparison to English, fewer benchmark results have been published in German.

## Considerations for selection

- Speaker Independent
- Continuous and Spontaneous Speech
- Large Vocabulary
- Open Sourced and pretrained

## Selected Models

- wav2vec2.0
- Conformer Transducer
- Conformer CTC
- Quartznet
- ContextNet
- Citrinet
- Speechbrain
  
## Model wav2vec2.0

- This model is by facebook AI research (FAIR)
- There are several pretrained model are available on huggingface
- Different finetuned versions of this model on lastest common voice datasets (V-6.0, V-7.0, V-8.0, V-9.0 ) are also available
- We have selected one pretrained model wav2vec2 large xlsr-53-german by facebook
- And a fine-tuned version on Commonvoice (6.0) facebook wav2vec2 large xlsr-53-german by Jonatas Grosman
- Since it had the lowest self-reported WER on Common Voice (12.06%) compared to 18.5% reported for the original
model provided by FAIR

## Why XLSR-53

The model facebook wav2vec2 large xlsr-53-german is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language.

- It is multilingual pre-trained wav2vec 2.0 (XLSR)
- Architecture is based on Transformers’ encoder
- Datasets on which a pre-trained model was trained (Multilingual LibriSpeech, Common Voice, Babel)

## Model usage

- We can find this model easily in transformers python library.
- To download and use any of the pretrained models for our given task
- We  just need to use few lines of codes (PyTorch version)

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

Link to [original](https://huggingface.co/facebook/wav2vec2-large-xlsr-53-german) and [finetuned](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-german) model
