from azure.storage.blob import BlobServiceClient

def scan_azure_bucket(bucket_url, conn_str):
    container_name = bucket_url.replace("azure://", "")
    print(f"[Azure] Scanning container: {container_name}")

    try:
        client = BlobServiceClient.from_connection_string(conn_str)
        container = client.get_container_client(container_name)
        props = container.get_container_properties()

        if props['public_access']:
            print(f"❗ Public Access Detected: {container_name}")
        else:
            print(f"[+] {container_name} is secure.")
    except Exception as e:
        print(f"Error: {e}")