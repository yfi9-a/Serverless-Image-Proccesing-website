# 📷 Serverless Image Processor – Architecture Documentation
This solution implements a **serverless image upload and processing architecture** using:

- **Amazon S3**
- **API Gateway**
- **AWS Lambda**

It enables users to upload images via a static frontend hosted on S3. Upon upload, Lambda is triggered to process and resize the image, storing the output in a separate bucket.

The **API Gateway + Lambda** approach provides a secure interface to generate presigned PUT URLs, avoiding public write access to S3. The event-driven backend allows fully automated image processing.

### ✅ Services Used:

- Amazon S3 (static hosting + object storage)
- Amazon API Gateway (REST API)
- AWS Lambda (presigned URL + image resize)

This design is **simple, scalable, and cost-effective**.

---

## 🗺️ Default Architecture




![Architecture](images/Diagram.drawio(1).png)

---

## 🛠️ Deployment Stack

This solution can be deployed **manually using the AWS Console/CLI**, or later **codified using AWS CDK**.

| Component          | Technology Used                    |
|-------------------|------------------------------------|
| Web UI            | Amazon S3 (Static Website Hosting) |
| Upload Interface  | API Gateway + Lambda               |
| Image Storage     | Amazon S3 (Private Buckets)        |
| Processing        | Lambda (Python + Pillow)           |
| Security          | IAM Roles (scoped permissions)     |
| Event Trigger     | S3 Event Notification to Lambda    |

---

## 🔐 Security & 💰 Cost Optimization

This solution is optimized for **minimal cost** and **strong security**:

- ✅ All S3 buckets are **private** by default
- ✅ Only static web UI bucket is **publicly readable**
- ✅ **Presigned URLs** are short-lived (60 seconds)
- ✅ No **NAT Gateway** or public internet for Lambda
- ✅ Can use **VPC Endpoint** for private S3 access (optional)

---

## 🌟 Optional Enhancements

- CloudFront + OAI for secure & fast delivery of processed images
- DynamoDB to store metadata or upload logs
- Cognito for user authentication
- S3 Lifecycle Rules for cost optimization & archival

---
