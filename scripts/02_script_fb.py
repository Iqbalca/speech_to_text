import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53-german")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-xlsr-53-german")

###import IPython.display as display
###display.Audio("sample_clip1.mp3", autoplay=True )

#load any audio file with 16KHZ sampling rate
speech, rate = librosa.load("con_audio_2-Copy1.wav",sr=16_000)
input_values = processor(speech, return_tensors = 'pt').input_values #input_values speech to the tokenizer
#Store logits (non-normalized predictions)
logits = model(input_values).logits

#Store predicted values
predicted_ids = torch.argmax(logits, dim =-1)

#decode the audio to generate text
transcriptions = processor.decode(predicted_ids[0])

print(transcriptions)
