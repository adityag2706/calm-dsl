from calm.dsl.constants import PROVIDER
from calm.dsl.builtins import Account, AwsAccountSpec


class AwsSpec(AwsAccountSpec):

    access_key_id = "aws_access_key"
    secret_access_key = "aws_secret_access_key"
    regions = [
        {
            "name": "us-east-1",
            "images": [
                "fedora-coreos-30.20190914.dev.0-hvm",
                "fedora-coreos-32.20200925.20.1",
                "fedora-coreos-32.20200506.10.0",
            ],
        }
    ]


class AwsAccount(Account):
    provider_type = PROVIDER.ACCOUNT.AWS
    spec = AwsSpec
