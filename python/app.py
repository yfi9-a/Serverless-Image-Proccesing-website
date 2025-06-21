from PIL import Image
import boto3
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    img_obj = s3.get_object(Bucket=bucket, Key=key)
    img = Image.open(io.BytesIO(img_obj['Body'].read()))
    resized = img.resize((500, int(img.height * 500 / img.width)))

    buffer = io.BytesIO()
    resized.save(buffer, format="JPEG")
    buffer.seek(0)

    s3.put_object(Bucket='procecssed-images-for-manaraproject', Key=f"resized/{key.split('/')[-1]}", Body=buffer, ContentType="image/jpeg")

    return {"status": "done"}
