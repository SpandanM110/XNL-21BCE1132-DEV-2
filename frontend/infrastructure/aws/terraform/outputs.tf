output "vpc_id" {
  value = aws_vpc.main.id
}

output "eks_cluster_id" {
  value = aws_eks_cluster.eks_cluster.id
}

output "eks_cluster_endpoint" {
  value = aws_eks_cluster.eks_cluster.endpoint
}
