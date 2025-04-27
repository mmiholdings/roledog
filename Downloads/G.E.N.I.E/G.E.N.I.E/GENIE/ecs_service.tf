resource "aws_ecs_cluster" "genie_cluster" {
  name = "genie-cluster"
}

resource "aws_ecs_service" "genie_service" {
  name            = "genie-service"
  cluster         = aws_ecs_cluster.genie_cluster.id
  task_definition = aws_ecs_task_definition.genie_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets         = ["<YOUR_SUBNET_ID>"]
    security_groups = ["<YOUR_SECURITY_GROUP_ID>"]
    assign_public_ip = true
  }
}