# Install required libraries
!pip install diffusers transformers accelerate safetensors

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

# Load base model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    safety_checker=None,  # disable NSFW filter if using NSFW LoRA
).to("cuda")

# Download your LoRA model (replace with actual URL)
import requests
lora_url = "https://example.com/path/to/nsfw_lora_wan_14b_e15.safetensors"
lora_path = "./nsfw_lora_wan_14b_e15.safetensors"
response = requests.get(lora_url)
with open(lora_path, "wb") as f:
    f.write(response.content)

# Apply LoRA using PEFT (or custom hooks — this part needs more details)
# Note: diffusers does not natively support .safetensors LoRA, you'll need a custom loader or use WebUI like AUTOMATIC1111

# Generate image
prompt = "A beautiful Indian model in traditional dress, ultra-realistic, 8K, soft lighting"
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]

# Save image
image.save("output.png")
