variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region to deploy resources in"
  type        = string
  default     = "asia-southeast1"
}

variable "db_password" {
  description = "Password for the database user"
  type        = string
  sensitive   = true
}

variable "db_instance_name" {
  description = "Name of the Cloud SQL instance"
  type        = string
}
