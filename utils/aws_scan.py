import boto3
import botocore

def scan_aws_bucket(bucket_url, aws_key, aws_secret):
    bucket_name = bucket_url.replace("s3://", "")
    print(f"[AWS] Scanning bucket: {bucket_name}")

    try:
        s3 = boto3.client('s3', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            if grant['Grantee'].get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                print(f"❗ Public Access Detected: {bucket_name}")
            else:
                print(f"[+] {bucket_name} is secure.")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e}")