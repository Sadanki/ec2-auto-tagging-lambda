import boto3
import datetime

def lambda_handler(event, context):
    print("Received event:", event)

    ec2 = boto3.client('ec2')
    
    try:
        instance_id = event['detail']['instance-id']
        current_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')

        tags = [
            {'Key': 'LaunchDate', 'Value': current_date},
            {'Key': 'Environment', 'Value': 'Development'}
        ]

        ec2.create_tags(Resources=[instance_id], Tags=tags)
        print(f"Tagged instance {instance_id} with: {tags}")

        return {
            'statusCode': 200,
            'body': f"Instance {instance_id} tagged successfully."
        }

    except KeyError as e:
        print(f"Missing expected event key: {str(e)}")
        return {
            'statusCode': 400,
            'body': f"Event missing key: {str(e)}"
        }
