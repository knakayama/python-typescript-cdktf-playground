from typing import Optional

import boto3


class UserDriver:
    def __init__(self, table_name: str, endpoint_url: Optional[str] = None) -> None:
        self.resource = boto3.resource("dynamodb", endpoint_url=endpoint_url)
        self.table = self.resource.Table(table_name)
