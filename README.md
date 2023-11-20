# The Daily Blend

Curated newsreader with offline functionality

## Local Development

## Deployment

Create a PlanetScale SQL database. This database was chosen for its price and performance.

Create an AWS S3 bucket to store code artefacts.

Enter the following secrets on AWS Secrets Manager:

```
PlanetScaleDBCredentials: host, username, password, dbname
```

Enter the following secrets on Github Secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
S3_ARTEFACTS_BUCKET
```

Run the Github pipeline and it will provision the infrastructure.

Use AWS Route 53 to point your DNS at the application.
