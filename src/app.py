import requests

API_TOKEN='dps eu troco' 

url = "https://api-inference.huggingface.co/models/gpt2"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

data = {
    "inputs": "Boa Noite"
}

response = requests.post(url, headers=headers, json=data)
print(f"URL usada: {url}")
print("Status:", response.status_code)
print("Resposta bruta:", response.text)