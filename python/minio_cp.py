from minio import Minio
from minio.error import S3Error

# MinIO server credentials
MINIO_URL = "127.0.0.1:9000"  # or your MinIO server URL
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"

# Initialize the MinIO client
minio_client = Minio(
    MINIO_URL,
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False  # Set to False if you are not using HTTPS
)

# File to upload
file_path = "./file2.txt"
bucket_name = "state-terraform-s3"
object_name = "file2.txt"

# Ensure the bucket exists
found = minio_client.bucket_exists(bucket_name)
if not found:
    minio_client.make_bucket(bucket_name)
else:
    print(f"Bucket '{bucket_name}' already exists")

# Upload the file
try:
    minio_client.fput_object(
        bucket_name, object_name, file_path
    )
    print(f"'{file_path}' is successfully uploaded as '{object_name}' to bucket '{bucket_name}'.")
except S3Error as err:
    print(f"Error occurred: {err}")

