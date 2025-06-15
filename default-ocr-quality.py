from PIL import Image
import torch
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="Qwen/Qwen2.5-VL-3B-Instruct", device="cpu")
claim_number_json = pipe([{"role": "user", "content": [{"type": "image", "image": Image.open("eob-example.png")}, {"type": "text", "content": "What's the claim number, in JSON?"}]}, {"role": "assistant", "content": [{"type": "text", "text": '{"claim_number": "'}]}], max_new_tokens=500)
print(claim_number_json[-1]['generated_text'][-1]['content'][0]['text'])
