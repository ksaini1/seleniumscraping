import boto3
ec2 = boto3.resources('ec2')
instance = ec2.create_instance(
    ImageId=''
)