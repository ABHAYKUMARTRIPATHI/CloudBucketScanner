from google.cloud import storage
import os

def scan_gcp_bucket(bucket_url, credentials_path):
    bucket_name = bucket_url.replace("gs://", "")
    print(f"[GCP] Scanning bucket: {bucket_name}")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    client = storage.Client()

    try:
        bucket = client.get_bucket(bucket_name)
        policy = bucket.get_iam_policy()
        for role in policy.bindings:
            if "allUsers" in role["members"]:
                print(f"❗ Public Access Detected: {bucket_name}")
                return
        print(f"[+] {bucket_name} is secure.")
    except Exception as e:
        print(f"Error: {e}")