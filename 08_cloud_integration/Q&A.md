# Cloud Integration Q&A

**Q: Which cloud platform should I use?**
A: It depends on your needs:
- GCP: Best data analytics integration, pay-per-second
- AWS: Most mature, largest ecosystem
- Azure: Best for Microsoft stack users

**Q: How do I secure cloud credentials?**
A:
- Use service accounts, never hardcode keys
- Store credentials in environment variables
- Use IAM roles with least privilege
- Rotate keys regularly

**Q: How much will cloud infrastructure cost?**
A:
- Use cost calculators
- Monitor actual usage
- Use spot/preemptible instances
- Set up billing alerts

**Q: How do I optimize cluster costs?**
A:
- Right-size instances
- Use auto-scaling
- Leverage spot instances
- Delete idle clusters

**Q: How do I access cloud storage from Spark?**
A: Each platform has specific connectors:
- GCP: gs:// (Google Cloud Storage)
- AWS: s3a:// (S3)
- Azure: wasbs:// (Blob Storage)

**Q: What about data transfer costs?**
A: Keep data in same region/zone as cluster
