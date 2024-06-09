
variable "minio_region" {
  description = "Default MINIO region"
  default     = "us-east-1"
}

variable "minio_server" {
  description = "The MinIO server endpoint"
  type        = string
  sensitive   = false
  default     = "192.168.1.178:9000" 
}

variable "minio_user" {
  description = "MINIO user"
  default     = "minioadmin"
}

variable "minio_password" {
  description = "MINIO password"
  default     = "minioadmin"
}