import requests
import json
from gtts import gTTS

# Define the API endpoint and parameters
api_url = "https://api.openai.com/v1/chat/completions"
api_key = "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"
api_ver = "gpt-4"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
ask = input()

data = {
    "model": api_ver,
    "messages": [{"role":"user", "content":ask}],
}

# Send the HTTP request and receive the response
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Print the response
res = response.json()

msg = res['choices'][0]['message']['content']
tts = gTTS(msg, lang="en", slow=False)
tts.save("response.mp3")