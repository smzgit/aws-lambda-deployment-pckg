mkdir "lambda_pckg"
cp -r complete_code/ lambda_pckg/
pip install -r requirements.txt -t lambda_pckg/
zip -r lambda_deployment_pckg.zip lambda_pckg/
rm -rf lambda_pckg/