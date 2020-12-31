import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

response = client.get_group(
    GroupName='admin',
    Marker='string',
    MaxItems=123
)

print(response)