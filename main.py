import requests

urlDiscord = "https://discord.com/api/webhooks/1361600447256727642/q2Sq8rBBlGiu5TFJQ4qyFUS8IESXjCY5SR_b-k2vTlNLXUFL_oVxu26TBiIBb8I3KbK9"

message = {
    "content": "Hello from Python!"
}

requests.post(urlDiscord, json=message)


