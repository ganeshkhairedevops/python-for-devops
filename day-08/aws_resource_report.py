import boto3
import json


def get_ec2_instances(): # Fetches a list of EC2 instances and their states
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })

    return instances


def get_s3_buckets(): # Fetches a list of S3 buckets
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    buckets = []
    for bucket in response["Buckets"]:
        buckets.append(bucket["Name"])

    return buckets


def main(): # Main function to generate AWS resource report
    print("Fetching AWS resources...\n")

    ec2_instances = get_ec2_instances()
    s3_buckets = get_s3_buckets()

    aws_report = {
        "EC2_Instances": ec2_instances,
        "S3_Buckets": s3_buckets
    }

    # Print to terminal
    print("EC2 Instances:")
    for instance in ec2_instances:
        print(f"  {instance['InstanceId']} - {instance['State']}")

    print("\nS3 Buckets:")
    for bucket in s3_buckets:
        print(f"  {bucket}")

    # Save to JSON file
    with open("aws_report.json", "w") as file:
        json.dump(aws_report, file, indent=4)

    print("\nAWS resource report saved to aws_report.json")


if __name__ == "__main__":
    main()
