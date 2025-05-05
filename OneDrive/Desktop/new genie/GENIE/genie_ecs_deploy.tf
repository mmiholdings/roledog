
provider "aws" {
  region = "us-east-2"
}

resource "aws_ecs_cluster" "genie_cluster" {
  name = "genie-ecs-cluster"
}

resource "aws_ecs_task_definition" "genie_task" {
  family                   = "genie-task"
  requires_compatibilities = ["FARGATE"]
  network_mode            = "awsvpc"
  cpu                     = "256"
  memory                  = "512"
  execution_role_arn      = aws_iam_role.ecs_task_execution.arn

  container_definitions = jsonencode([
    {
      name      = "genie"
      image     = "682033469983.dkr.ecr.us-east-2.amazonaws.com/genie3:latest"
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [{
        containerPort = 8080
        protocol      = "tcp"
      }]
    }
  ])
}

resource "aws_iam_role" "ecs_task_execution" {
  name = "ecsTaskExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        },
        Effect = "Allow",
        Sid = ""
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_exec_policy" {
  role       = aws_iam_role.ecs_task_execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_ecs_service" "genie_service" {
  name            = "genie-service"
  cluster         = aws_ecs_cluster.genie_cluster.id
  task_definition = aws_ecs_task_definition.genie_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-xxxxxxxx"] # Replace with your subnet
    security_groups = ["sg-xxxxxxxx"]     # Replace with your SG
    assign_public_ip = true
  }
}
