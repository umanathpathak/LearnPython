import boto3

s3 = boto3.resource('s3')
s3_c = boto3.client('s3')

autoserver = s3.Object(bucket_name='autoserver',key='boto3.pdf')
print(autoserver.bucket_name)
print(autoserver.key)

#s3.Bucket('autoserver').list_objects()
#s3.Bucket('autoserver').get_object(Key='boto3.pdf')