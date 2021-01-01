import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

iam_all_access_keys = client.list_access_keys(
    UserName='fharenheit',
    Marker='string',
    MaxItems=123
)

print(iam_all_access_keys)
