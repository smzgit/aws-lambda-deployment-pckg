# aws-lambda-deployment-pckg
Convert any python git repo into AWS - Lambda deployment package, basically a zip file which can be uploaded directly or on S3

### Steps - 
1. Dump all the code in `complete_code` directory, remember the path to your lambda handler.
2. Run `chmod +x lambda_build.sh` & then run `./lambda_build.sh`
3. Above step will create a zip file named _lambda_deployment_pckg_.
4. Upload the deployment package,`lambda_deployment_pckg.zip`, to AWS Lambda directly or via S3,if the size is large.