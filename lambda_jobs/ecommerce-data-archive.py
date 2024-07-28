import json
import boto3

source_bucket_name = 'ecommerce-data-yb'
destination_bucket_name = 'ecommerce-data-archive-yb'

def lambda_handler(event, context):
    # TODO implement
    
    print('Event: ',event)
    
    
    # Extract the message from the SNS notification
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    # Access the details dict within the message
    detail = message['detail']
    
    # Extract the value of the "state" key
    glue_job_status = detail['state']
    
    print(f"Glue Job Status: {glue_job_status}")
    
    if glue_job_status == "SUCCEEDED":
        if not source_bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing Source bucket in the event!')
            }
        
        # Create S3 Client
        s3 = boto3.client('s3')
        
        try:
            # call transfer_files function (defined below)
            transfer_files(s3, source_bucket_name, destination_bucket_name)
            return {
                'statusCode': 200,
                'body': json.dumps('File Archied Successfully!')
            }
        
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error in Archiving file: {e}')
            }
        
        else:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Glue Job {glue_job_status}: {event}')
            }
            
    
def transfer_files(s3, source_bucket, destination_bucket):
    for obj in s3.list_objects_v2(Bucket=source_bucket)['Contents']:
        source_key = obj['Key']
        destination_key = source_key
        
        s3.copy_object(CopySource={'Bucket':source_bucket, 'Key':source_key},
                        Bucket=destination_bucket, Key=destination_key)
        
        print(f"Copied {source_key} to {destination_bucket}/{destination_key}")