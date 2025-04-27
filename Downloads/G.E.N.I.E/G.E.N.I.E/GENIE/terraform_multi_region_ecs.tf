
variable "regions" {
  default = ["us-east-1", "us-east-2"]
}

module "ecs_genie" {
  for_each = toset(var.regions)

  source = "./modules/ecs"
  region = each.value
}
