provider "google" {
  credentials = file("${path.module}/creds.json")
  project     = var.project_id
  region      = var.region
}
