# Cloud Bucket Misconfiguration Scanner

## 🔍 Overview
This tool scans cloud buckets (AWS S3, Google Cloud, Azure Blob) for misconfigurations like public access, anonymous listing, and sensitive file exposure.

## ✅ Features
- Multi-cloud support (AWS, GCP, Azure)
- API key prompts for each service
- Public access detection
- Simple, CLI-based usage

## 🧰 Requirements
- Python 3.7+
- Run `pip install -r requirements.txt`

## 🚀 Usage
1. Add your cloud buckets to `sample_buckets.txt` in this format:
s3://your-bucket-name
gs://your-gcp-bucket
azure://your-container-name

2. Run the tool:
python scanner.py

3.When prompted, enter:
	•	AWS Access Key ID & Secret
	•	Path to GCP JSON credentials
	•	Azure Blob Storage connection string

##🔒 Note

Always secure your credentials. Avoid sharing or hardcoding them in code.

## 👤 Author

**Abhay Kumar Tripathi**  
[GitHub](https://github.com/ABHAYKUMARTRIPATHI)  
[LinkedIn](https://www.linkedin.com/in/abhay-kumar-tripathi-54899b31a)  
[Instagram](https://www.instagram.com/abhaytripathi_46)
