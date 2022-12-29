import requests


class ChatHttpClientDriver:
    def send(self, text: str, username: str, url: str) -> None:
        requests.post(
            url=url,
            data={
                "channel": "aws",
                "username": username,
                "icon_emoji": ":range:",
                "attachments": [
                    {
                        "text": text,
                    }
                ],
            },
        )
