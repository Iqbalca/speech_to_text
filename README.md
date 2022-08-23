# Speec to Text Recognition

#### This repository uses the huggingface and the transformers library

- The huggingface library is the most popular NLP library with over 68,000 starts on [github](https://github.com/huggingface/transformers)
- It provides state-of-the-art natural processing models and very clean API.
  
- Transformers library supports with a deep learning library like PyTorch, TensorFlow

- It supports Python 3.6+, PyTorch 1.1.0+, TensorFlow 2.0+, and Flax
  
- It can be used to perform Speech to Text Conversion in German Language


#### We have used different models for the transcription of audio files in German Language.


### Model 1:

>  Facebook wav2vec2 large xlsr-53

- It is multilingual pre-trained wav2vec 2.0 (XLSR)
- Architecture is based on Transformers’ encoder
- Datasets on which a pre-trained model was trained (Multilingual LibriSpeech, Common Voice, Babel)

Code can be found under the repo *speech_to_text/test/*

Link to the [model]() can be found [here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/wav2vec2) 

### Model 2: 

> Fine Tuned xlsr-53

- German dataset: Common Voice (Version 6.1) 

Common voice is a crowd-sourced read speech corpus and may have noisy dialogues. 
Link to the [model](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-german) can be found [here](https://github.com/jonatasgrosman/wav2vec2-sprint)



> 

