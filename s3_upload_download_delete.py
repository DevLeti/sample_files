"""
Region restriction
All service access is limited to the us-east-1 and us-west-2 Regions unless mentioned otherwise in the service details below.
If you load a service console page in another AWS Region you will see access error messages.
-> Education account: us-east-1, us-west-2만 가능

AWS credentials should be set -  "/.aws/credentials"
"""
import boto3
import time

s3 = boto3.client('s3')

# 미리 us-east, us-west 각각 하나씩 bucket을 만든 상태. 버킷의 이름을 가져와서 업로드 합니다.
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

def upload_file(size):
    # US-EAST
    sum_time=0
    average_time=0
    print("s3 bucket name with region, size: {}, {}, {}".format(buckets[0], "us-east-1", size))
    for i in range (1, 11):
        before=time.time()
        s3.upload_file("./{}/{}.txt".format(size,str(i)), buckets[0], "{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average upload time: {} seconds.".format(average_time))
    print()
    
    # US-WEST
    sum_time=0
    average_time=0
    print("s3 bucket name with region, size: {}. {}, {}".format(buckets[1], "us-west-2", size))
    for i in range (1, 11):
        before=time.time()
        s3.upload_file("./{}/{}.txt".format(size,str(i)), buckets[1], "{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average upload time: {} seconds.".format(average_time))
    print()

def download_file(size):
    # US-EAST
    sum_time=0
    average_time=0 
    print("s3 bucket name with region, size: {}. {}, {}".format(buckets[0], "us-east-1", size))
    for i in range (1,11):
        before=time.time()
        s3.download_file(buckets[0], "{}/{}.txt".format(size,str(i)), "./downloads/{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average download time: {} seconds.".format(average_time))
    print()

    #US-WEST
    sum_time=0
    average_time=0 
    print("s3 bucket name with region, size: {}. {}, {}".format(buckets[1], "us-west-2", size))
    for i in range (1,11):
        before=time.time()
        s3.download_file(buckets[1], "{}/{}.txt".format(size,str(i)), "./downloads/{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average download time: {} seconds.".format(average_time))
    print()

def delete_file(size):
    # US-EAST
    sum_time=0
    average_time=0 
    print("s3 bucket name with region, size: {}. {}, {}".format(buckets[0], "us-east-1", size))
    for i in range (1,11):
        before=time.time()
        s3.delete_object(Bucket=buckets[0], Key="{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average delete time: {} seconds.".format(average_time))
    print()

    #US-WEST
    sum_time=0
    average_time=0 
    print("s3 bucket name with region, size: {}. {}, {}".format(buckets[1], "us-west-2", size))
    for i in range (1,11):
        before=time.time()
        s3.delete_object(Bucket=buckets[1], Key="{}/{}.txt".format(size,str(i)))
        after=time.time()
        sum_time = sum_time + (after - before)
    average_time = round(sum_time / 10, 5)
    print("average delete time: {} seconds.".format(average_time))
    print()



upload_file("1kb")
upload_file("10kb")
upload_file("1mb")
upload_file("10mb")

download_file("1kb")
download_file("10kb")
download_file("1mb")
download_file("10mb")

delete_file("1kb")
delete_file("10kb")
delete_file("1mb")
delete_file("10mb")
