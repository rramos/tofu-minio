output "minio_id" {
  value = minio_s3_bucket.state_terraform_s3.id
}

output "minio_url" {
  value = minio_s3_bucket.state_terraform_s3.bucket_domain_name
}

output "minio_txt_file" {
  value = minio_s3_object.txt_file.id
}
