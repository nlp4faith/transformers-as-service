import requests
import json

if __name__ == "__main__":
    question = "some texts"

    s = requests.post('http://127.0.0.1:8125/encode', json={"id": 123, "texts": [question]})
    print(s, s.text)