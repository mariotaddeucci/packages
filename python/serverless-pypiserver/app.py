from  serverless_pypiserver import Bucket
from botocore.client import Config

Bucket.setup(
    bucket='pypi',
    client={
        'endpoint_url': 'http://localhost:9000',
        'aws_access_key_id': 'minioadmin',
        'aws_secret_access_key': 'minioadmin',
        'config': Config(signature_version='s3v4'),
        'region_name': 'us-east-1'
    },
    packages_dir='packages'
)

pkg = Bucket.packages('sqlpipe')
print(pkg)
Bucket.get_file_url(pkg['filename'])

