
provider "aws" {
  region = "us-east-2"
}

resource "aws_ecs_cluster" "genie_monitoring" {
  name = "genie-monitoring-cluster"
}

resource "aws_ecs_task_definition" "streamlit_task" {
  family                   = "streamlit-task"
  requires_compatibilities = ["FARGATE"]
  network_mode            = "awsvpc"
  cpu                     = "256"
  memory                  = "512"
  execution_role_arn      = aws_iam_role.ecs_execution.arn

  container_definitions = jsonencode([
    {
      name      = "genie-audit-dashboard",
      image     = "streamlit/streamlit:latest",
      essential = true,
      portMappings = [{
        containerPort = 8501,
        protocol      = "tcp"
      }],
      command: ["streamlit", "run", "/app/streamlit_audit_dashboard.py", "--server.port=8501"]
    }
  ])
}

resource "aws_ecs_service" "streamlit_service" {
  name            = "genie-dashboard"
  cluster         = aws_ecs_cluster.genie_monitoring.id
  task_definition = aws_ecs_task_definition.streamlit_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-abc123"]     # Replace with your subnet
    security_groups = ["sg-abc123"]         # Replace with your SG
    assign_public_ip = true
  }
}

resource "aws_iam_role" "ecs_execution" {
  name = "genie-streamlit-ecs-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_policy" {
  role       = aws_iam_role.ecs_execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
