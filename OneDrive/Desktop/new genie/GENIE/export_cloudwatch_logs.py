
import boto3
import datetime

def export_logs(group_name, stream_name, file_name="genie_logs.txt"):
    logs = boto3.client('logs', region_name='us-east-2')
    end_time = int(datetime.datetime.now().timestamp() * 1000)
    start_time = end_time - (7 * 24 * 60 * 60 * 1000)  # 7 days

    events = logs.get_log_events(
        logGroupName=group_name,
        logStreamName=stream_name,
        startTime=start_time,
        endTime=end_time,
        startFromHead=True
    )

    with open(file_name, "w") as f:
        for e in events['events']:
            f.write(e['message'] + '\n')

    print(f"Exported logs to {file_name}")
