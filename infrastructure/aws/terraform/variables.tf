variable "aws_region" {
  description = "The AWS region to deploy resources"
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "VPC CIDR Block"
  default     = "10.0.0.0/16"
}

variable "subnet_cidrs" {
  description = "List of subnet CIDRs"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "eks_cluster_name" {
  description = "EKS Cluster Name"
  default     = "my-eks-cluster"
}
