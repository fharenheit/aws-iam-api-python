import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

response = client.create_user(
    Path='/',
    UserName='fharenheit6',
    PermissionsBoundary='blahblahblahblahblah',
    Tags=[
        {
            'Key': 'user',
            'Value': 'test'
        },
    ]
)

print(response)
