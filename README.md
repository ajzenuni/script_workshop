# script_workshop
 API Scripting Workshop - Python Requests (GET/POST/DELETE) Example
 
 # Requirements
Install the required modules running 'pip install -r stable-req.text'

# Get Started
Provide the tenant/environment url, api-token and username params in the auth_param_example.yaml file found in etc/. Rename the file to auth_param.yaml.

NOTE: the tenant url should not end with a '/'.  
NOTE: the api token should have the following permissions: Read configuration and Write configuration

tenant/environment url  
managed: https://{your-domain}/e/{your-environment-id}  
saas:  https://{your-environment-id}.live.dynatrace.com

# Executing
python request_example.py --script {get_host/post_tag/delete_tag} --tag {tag}

NOTE: May take some time to publish the dashboards to your environment

