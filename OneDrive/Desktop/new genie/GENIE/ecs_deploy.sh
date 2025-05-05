#!/bin/bash
aws ecs register-task-definition --cli-input-json file://ecs/ecs_task_definition.json
aws ecs update-service --cluster genie-cluster --service genie-service --force-new-deployment