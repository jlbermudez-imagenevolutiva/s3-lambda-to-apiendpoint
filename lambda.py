import boto3
import json

def lambda_handler(event, context):
  """This function sends a message to an HTTPS endpoint when a file is created in an S3 bucket.

  Args:
    event: The event object from AWS Lambda.
    context: The context object from AWS Lambda.

  Returns:
    None.
  """

  # Get the bucket name from the event object.
  bucket_name = event['Records'][0]['s3']['bucket']['name']

  # Get the object key from the event object.
  object_key = event['Records'][0]['s3']['object']['key']

  # Get the current time.
  now = datetime.now()

  # Get the file size from the event object.
  file_size = event['Records'][0]['s3']['object']['size']

  # Get the file hash from the event object.
  file_hash = event['Records'][0]['s3']['object']['eTag']

  # Create a JSON object containing the bucket name, object key, time, file size, and file hash.
  data = {
    'bucket_name': bucket_name,
    'object_key': object_key,
    'time': now.isoformat(),
    'file_size': file_size,
    'file_hash': file_hash
  }

  # Send the message to the HTTPS endpoint.
  requests.post(endpoint, data=json.dumps(data))

  return None