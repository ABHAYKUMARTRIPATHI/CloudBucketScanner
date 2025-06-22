import os
from utils.aws_scan import scan_aws_bucket
from utils.gcp_scan import scan_gcp_bucket
from utils.azure_scan import scan_azure_bucket

def main():
    print("=== Cloud Bucket Misconfiguration Scanner ===")

    aws_key = input("Enter your AWS Access Key ID: ")
    aws_secret = input("Enter your AWS Secret Access Key: ")
    gcp_key_path = input("Enter path to your GCP credentials JSON: ")
    azure_conn_str = input("Enter Azure Storage connection string: ")

    with open("sample_buckets.txt", "r") as file:
        buckets = file.read().splitlines()

    for bucket in buckets:
        if bucket.startswith("s3://"):
            scan_aws_bucket(bucket, aws_key, aws_secret)
        elif bucket.startswith("gs://"):
            scan_gcp_bucket(bucket, gcp_key_path)
        elif bucket.startswith("azure://"):
            scan_azure_bucket(bucket, azure_conn_str)
        else:
            print(f"Unknown bucket format: {bucket}")

if __name__ == "__main__":
    main()