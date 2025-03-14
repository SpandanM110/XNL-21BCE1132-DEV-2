resource "aws_autoscaling_group" "eks_autoscaler" {
  name                = "eks-autoscaler"
  max_size            = 5
  min_size            = 2
  desired_capacity    = 2
}
