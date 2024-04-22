import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("cat.jpg")
print(output[0]["generated_text"])  # Accessing the value associated with the key "generated_text"


