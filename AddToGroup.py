import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

response = client.add_user_to_group(
    GroupName='admin',
    UserName='fharenheit4'
)

print(response)