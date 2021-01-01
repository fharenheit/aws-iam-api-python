import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

response = client.delete_access_key(
    UserName='fharenheit',
    AccessKeyId='nNxqJrqxHCfpbHbH'
)

print(response)