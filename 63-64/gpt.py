import requests

class YandexGPT:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog

    def send_translate(self, text):
        url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": "es",
            "format": "HTML",
            "texts": [
                f"{text}"
            ],
            "folderId": f"{self.catalog}",
            "speller": False
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }


        response = requests.post(url, headers=headers, json=payload)
        text = response.json()['result']['alternatives'][0]['message']['text']
        return text
