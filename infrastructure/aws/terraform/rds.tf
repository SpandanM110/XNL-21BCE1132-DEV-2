resource "aws_db_instance" "primary_db" {
  identifier = "primary-db"
  engine = "mysql"
  instance_class = "db.t3.micro"
  allocated_storage = 20
  storage_type = "gp2"
  username = "admin"
  password = "password123"
  multi_az = true
  publicly_accessible = false
}
