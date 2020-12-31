import boto3

client = boto3.client('iam',
                      aws_access_key_id='admin',
                      aws_secret_access_key='admin123',
                      endpoint_url='http://localhost:8080/iam',
                      region_name='korea'
                      )

iam_all_users = client.list_users(MaxItems=200)
for user in iam_all_users['Users']:
    print(user['UserName'])