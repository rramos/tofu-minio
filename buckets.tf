resource "minio_s3_bucket" "state_terraform_s3" {
  bucket = "state-terraform-s3"
  acl    = "public"
}

resource "minio_s3_object" "txt_file" {
  depends_on  = [minio_s3_bucket.state_terraform_s3]
  bucket_name = minio_s3_bucket.state_terraform_s3.bucket
  object_name = "text.txt"
  content     = "Lorem ipsum dolor sit amet."
}

resource "minio_s3_bucket_versioning" "bucket" {
  depends_on = [minio_s3_bucket.state_terraform_s3]
  bucket     = minio_s3_bucket.state_terraform_s3.bucket

  versioning_configuration {
    status = "Enabled"
  }
}


