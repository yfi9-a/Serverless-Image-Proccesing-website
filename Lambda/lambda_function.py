import boto3
import urllib.parse
import io
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    record = event['Records'][0]
    source_bucket = record['s3']['bucket']['name']
    raw_key = record['s3']['object']['key']
    source_key = urllib.parse.unquote_plus(raw_key)

    destination_bucket = 'processed-images-for-manaraproject'
    destination_key = f"resized/{source_key.split('/')[-1]}"

    # Read image from S3
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image_data = response['Body'].read()
    
    # Resize image
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((500, int(image.height * 500 / image.width)))

    # Save resized image to buffer
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    # Upload to S3
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=buffer, ContentType='image/jpeg')

    print(f"Image resized and uploaded to {destination_bucket}/{destination_key}")
    return {'status': 'resized'}