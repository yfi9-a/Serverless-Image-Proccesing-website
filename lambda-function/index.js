const AWS = require('aws-sdk');
const S3 = new AWS.S3();
const sharp = require('sharp');

exports.handler = async (event) => {
  try {
    const record = event.Records[0];
    const srcBucket = record.s3.bucket.name;
    const srcKey = decodeURIComponent(record.s3.object.key.replace(/\+/g, " "));
    const dstBucket = "procecssed-images-for-manaraproject";

    console.log(`New image uploaded: ${srcKey}`);

    const originalImage = await S3.getObject({
      Bucket: srcBucket,
      Key: srcKey,
    }).promise();

    const resizedImage = await sharp(originalImage.Body)
      .resize({ width: 500 })
      .toBuffer();

    const fileName = srcKey.split("/").pop();
    const dstKey = `resized/${fileName}`;

    await S3.putObject({
      Bucket: dstBucket,
      Key: dstKey,
      Body: resizedImage,
      ContentType: 'image/jpeg',
    }).promise();

    console.log(`=> Processed image saved to ${dstBucket}/${dstKey}`);
  } catch (err) {
    console.error("=> Error processing image:", err);
    throw err;
  }
}
