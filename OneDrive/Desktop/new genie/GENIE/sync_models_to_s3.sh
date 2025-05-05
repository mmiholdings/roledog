#!/bin/bash
DATE=$(date +%Y-%m-%d)
aws s3 cp ppo_mo_agent.zip s3://genie-trained-models/$DATE/ppo_mo_agent.zip
aws s3 cp buffer/mes_buffer.json s3://genie-trained-models/$DATE/mes_buffer.json