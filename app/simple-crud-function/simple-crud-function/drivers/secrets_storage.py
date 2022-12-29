from typing import Optional, cast
import boto3
from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef


class SecretsStorageDriver:
    cached_secrets: dict[str, GetSecretValueResponseTypeDef] = {}

    def __init__(self, endpoint_url: Optional[str] = None) -> None:
        self.client = boto3.client("secretsmanager", endpoint_url=endpoint_url)

    def __fetch_secret(self, secret_id: str) -> GetSecretValueResponseTypeDef:
        if secret_id in self.cached_secrets:
            # TODO: Seems mypy doesn't evaluate the if statement.
            # It just evaluates get method return value.
            return cast(
                GetSecretValueResponseTypeDef, self.cached_secrets.get(secret_id)
            )

        secret = self.client.get_secret_value(SecretId=secret_id)
        self.cached_secrets[secret_id] = secret
        return secret

    def fetch_chat_webhook_url(self) -> str:
        secret = self.__fetch_secret("WebHookUrl").get("SecretString")
        assert secret is not None
        return secret
