import os
from typing import Optional

import boto3


class UserDriver:
    def __init__(
        self,
        table_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
    ) -> None:
        table = table_name if table_name else os.environ["USER_TABLE"]
        self.resource = boto3.resource("dynamodb", endpoint_url=endpoint_url)
        self.table = self.resource.Table(table)
