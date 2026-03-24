import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')  # N. Virginia

def lambda_handler(event, context):
    try:
        # ---------------------------
        # START INSTANCES (Auto-Start)
        # ---------------------------
        start_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Start']},
                {'Name': 'instance-state-name', 'Values': ['stopped']}
            ]
        )

        start_ids = []
        for reservation in start_response['Reservations']:
            for instance in reservation['Instances']:
                start_ids.append(instance['InstanceId'])

        print("Instances to START:", start_ids)

        if start_ids:
            ec2.start_instances(InstanceIds=start_ids)
            print("Start command sent")
        else:
            print("No instances found to start")

        # ---------------------------
        # STOP INSTANCES (Auto-Stop)
        # ---------------------------
        stop_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
                {'Name': 'instance-state-name', 'Values': ['running']}
            ]
        )

        stop_ids = []
        for reservation in stop_response['Reservations']:
            for instance in reservation['Instances']:
                stop_ids.append(instance['InstanceId'])

        print("Instances to STOP:", stop_ids)

        if stop_ids:
            ec2.stop_instances(InstanceIds=stop_ids)
            print("Stop command sent")
        else:
            print("No instances found to stop")

        return {
            "statusCode": 200,
            "message": "Execution completed"
        }

    except Exception as e:
        print("Error:", str(e))
        raise
