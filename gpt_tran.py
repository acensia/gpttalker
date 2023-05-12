import json
import requests


# Define the API endpoint and parameters
api_url = "https://api.openai.com/v1/chat/completions"
api_key = "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"

mp3 =""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
ask = input()

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role":"user", "content":ask}],
}

# Send the HTTP request and receive the response
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Print the response
res = response.json()

msg = res['choices'][0]['message']['content']