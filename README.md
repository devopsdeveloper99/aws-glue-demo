# AWS Glue 4.0 Container Demo via GitHub Actions

This repository demonstrates how to run an **AWS Glue 4.0** job using a Docker container inside **GitHub Actions**.

## 🔧 Prerequisites

- AWS account credentials stored as GitHub Secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

## 🚀 Run the Workflow

1. Go to the **Actions** tab in your GitHub repository.
2. Select **Run AWS Glue Job** workflow.
3. Click **Run workflow** (manual trigger).

This workflow will start an AWS Glue 4.0 container locally in GitHub Actions and execute the script:
```
app/src/my_glue_script.py
```

You’ll see logs in the GitHub Actions console.
