import boto3

#First you need to tell which resource you are going to use.
s3 = boto3.resource('s3')


#Create bucket
#s3.create_bucket(Bucket='autoserver')
#s3.create_bucket(Bucket='autoclient')

#get a list of bucket
#for bucket in s3.buckets.all():
#    print(bucket)
#    print(type(bucket))
#    print(bucket.name)

#Upload file in s3
data = open('boto3.pdf','rb')
#s3.Bucket('autoserver').put_object(Key='boto3.pdf',Body=data)

#there is some encoding issue so text file also upload as binary file.
#data = open('notes.txt','rb')
#s3.Bucket('testauto').put_object(Key='notes.txt',Body=data)

#s3.Bucket('testauto').delete(key='notes.txt')