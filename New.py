# Install dependencies
!pip install diffusers transformers accelerate

# Login to Hugging Face if needed (replace with your token)
from huggingface_hub import notebook_login
notebook_login()

# Load model (this is SFW unless replaced with uncensored checkpoint)
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",  # Replace with uncensored or NSFW fine-tuned model
    use_auth_token=True
)

pipe.to("cuda")

# Generate an image
prompt = "a fantasy painting of a woman in a forest"
image = pipe(prompt).images[0]
image.show()
