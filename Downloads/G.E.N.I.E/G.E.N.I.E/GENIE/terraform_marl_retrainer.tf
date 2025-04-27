resource "aws_ecs_task_definition" "marl_trainer" {
  family                   = "genie-marl-trainer"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"

  container_definitions = jsonencode([{
    name  = "trainer"
    image = "ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/genie-marl-trainer:latest"
    portMappings = [{ containerPort = 8501, protocol = "tcp" }]
    essential = true
    environment = [
      { name = "ENV", value = "production" }
    ]
  }])
}

resource "aws_ecs_service" "marl_training_service" {
  name            = "marl-trainer-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.marl_trainer.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-abc123"]
    security_groups = ["sg-abc123"]
    assign_public_ip = true
  }
}