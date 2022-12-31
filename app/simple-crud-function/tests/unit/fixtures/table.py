import boto3


class TableFixture:
    def __init__(self, table_name: str, endpoint_url: str) -> None:
        self.resource = boto3.resource("dynamodb", endpoint_url=endpoint_url)
        self.table = self.resource.Table(table_name)

    def create_table(self) -> None:
        self.resource.create_table(
            TableName=self.table.name,
            KeySchema=[
                {
                    "AttributeName": "pk",
                    "KeyType": "HASH",
                },
                {
                    "AttributeName": "sk",
                    "KeyType": "RANGE",
                },
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "pk",
                    "AttributeType": "S",
                },
                {
                    "AttributeName": "sk",
                    "AttributeType": "S",
                },
                {
                    "AttributeName": "gsi1",
                    "AttributeType": "S",
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "gsi1",
                    "KeySchema": [
                        {
                            "AttributeName": "gsi1",
                            "KeyType": "HASH",
                        },
                    ],
                    "Projection": {
                        "ProjectionType": "ALL",
                    },
                },
            ],
            BillingMode="PAY_PER_REQUEST",
        )

    def delete_table(self) -> None:
        self.table.delete()
