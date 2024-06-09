#!/usr/bin/python

import duckdb

# MinIO server credentials
MINIO_URL = "127.0.0.1:9000"  # or your MinIO server URL
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
BUCKET_NAME = "state-terraform-s3"
OBJECT_NAME = "./sample_data.csv"

# MinIO endpoint
MINIO_ENDPOINT = f"https://{MINIO_URL}/{BUCKET_NAME}/{OBJECT_NAME}"

# DuckDB connection
con = duckdb.connect()

# Configuring DuckDB to use the MinIO S3-compatible storage
con.execute(f"""
SET s3_endpoint='{MINIO_URL}';
SET s3_access_key_id='{ACCESS_KEY}';
SET s3_secret_access_key='{SECRET_KEY}';
SET s3_region='us-east-1';  -- Specify the region, 'us-east-1' is default for MinIO
SET s3_use_ssl=true;  -- Use true if MinIO is set up with SSL, false otherwise
""")

# Create a table in DuckDB pointing to the CSV file stored in MinIO
con.execute(f"""
CREATE TABLE my_table AS
SELECT * FROM read_csv_auto('s3://{BUCKET_NAME}/{OBJECT_NAME}');
""")

# Query the table to verify
result = con.execute("SELECT * FROM my_table LIMIT 10").fetchall()
for row in result:
    print(row)

# Close the DuckDB connection
con.close()

