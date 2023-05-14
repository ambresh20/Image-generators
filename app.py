# openai.api_key = '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'

import openai

# DALL-E API key
openai.api_key = "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"

# The text prompt you want to use to generate an image
prompt = "a girl in forest wearing red cloths"

# Generate an image
response = openai.Image.create(
    prompt = prompt,
    model = "image-alpha-001",
    size = "256x256",
    n = 2,
    response_format = "url"
)

# Print the URL of the generated image
print(response["data"][1]["url"])
