resource "google_sql_database_instance" "pg_instance" {
  name             = var.db_instance_name
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true
      authorized_networks {
        name  = "IP-Connect-GCP-terraform"
        value = "124.122.86.147"
      }
    }
  }
}

resource "google_sql_user" "pg_user" {
  name     = "postgres"
  instance = google_sql_database_instance.pg_instance.name
  password_wo = var.db_password
}

resource "google_sql_database" "api_db" {
  name     = "api_db"
  instance = google_sql_database_instance.pg_instance.name
}
