import boto3, logging 

def lambda_handler(event, context):

    cfn_client = boto3.client('cloudformation')

    response = cfn_client.update_termination_protection(
        EnableTerminationProtection=True, 
        StackName=event["ResourceId"]
    )

    stack_id = response['StackId'] 

    logging.info(f"TERMINATION PROTECTION ENABLED ON CFN STACK WITH ID: {stack_id}")

