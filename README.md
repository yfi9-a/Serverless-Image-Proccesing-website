Architecture Diagram

This solution implements a serverless image upload and processing architecture using Amazon S3, API Gateway, and AWS Lambda. It enables users to upload images via a static frontend hosted on S3. Upon upload, Lambda is triggered to process and resize the image, storing the output in a separate bucket.

The API Gateway + Lambda approach provides a secure interface to generate presigned PUT URLs, avoiding public write access to S3. The event-driven backend allows fully automated serverless image processing.

The AWS implementation includes:
	•	Amazon S3 (static hosting + object storage)
	•	Amazon API Gateway REST API
	•	AWS Lambda (for both presigned URL generation and image processing)

Amazon S3 stores the original and processed images, while Lambda handles event-driven transformation. This design is simple, scalable, and cost-effective.

⸻

Default Architecture

⸻

Deployment Stack

You can deploy the solution manually using AWS Console or CLI. Alternatively, a future version can be codified using AWS CDK.

Component	Technology Used
Web UI	Amazon S3 (Static Website Hosting)
Upload Interface	API Gateway + Lambda
Image Storage	Amazon S3 (Private Buckets)
Processing	Lambda (Python + Pillow)
Security	IAM Roles with scoped permissions
Event Trigger	S3 Event Notification to Lambda


⸻

Security & Cost Optimization

This solution is optimized for minimal cost and strong security:
	•	✅ All S3 buckets are private by default
	•	✅ Only static web UI bucket is publicly readable
	•	✅ Presigned URLs are short-lived (60 seconds)
	•	✅ No NAT Gateway or Internet access from Lambda
	•	✅ VPC Endpoint can be added for private S3 access (optional)

⸻

Optional Enhancements

You can further enhance the system using:
	•	CloudFront + OAI for secure delivery of processed images
	•	DynamoDB to store metadata or image history
	•	Cognito for user authentication
	•	Lifecycle Rules on S3 for cost management

⸻
# Serverless-Image-Proccesing-website
