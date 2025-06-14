

# EC2 Auto Tagging Lambda

## Overview

This project contains an AWS Lambda function that automatically tags newly launched EC2 instances. Tagging helps with resource tracking, cost management, and organization within your AWS environment.

---

## Features

- Automatically tags EC2 instances as soon as they launch.
- Uses AWS Lambda and Boto3 (Python SDK for AWS).
- Simple and efficient automation for better resource management.

---

## Files

- `lambda_function.py`: The AWS Lambda function code to auto-tag EC2 instances.
- `Assignment 5.docx`: Assignment description and requirements.

---

## How to Deploy

1. Create an AWS Lambda function using Python 3.x runtime.
2. Copy and paste the code from `lambda_function.py` into your Lambda function.
3. Set up the appropriate IAM role with permissions:
   - `ec2:CreateTags`
   - `ec2:DescribeInstances`
4. Configure the Lambda function to trigger on EC2 instance launch events via CloudWatch Events (EventBridge).
5. Save and test the function by launching a new EC2 instance and verifying tags are applied automatically.

---

## Usage

- Launch EC2 instances as usual.
- The Lambda function will run automatically and add predefined tags to your instances.

---

## License

This project is for educational purposes.

---

## Contact

Created by Vignesh Sadanki  
GitHub: [https://github.com/Sadanki](https://github.com/Sadanki)
