import requests

JENKINS_USER = "harikalenkala"
JENKINS_TOKEN = "11d54a10f90ba4ad0a694a7a7b86ef6d13"

JENKINS_URL = "http://localhost:8080"

# Step 1: Get CSRF Crumb
crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
crumb_response = requests.get(crumb_url, auth=(JENKINS_USER, JENKINS_TOKEN))
crumb_data = crumb_response.json()

headers = {
    crumb_data['crumbRequestField']: crumb_data['crumb']
}

# Step 2: Trigger Job
build_url = f"{JENKINS_URL}/job/DevOpsDeckJob/build"
response = requests.post(build_url, auth=(JENKINS_USER, JENKINS_TOKEN), headers=headers)

if response.status_code in [200, 201]:
    print("✅ Jenkins build triggered successfully!")
else:
    print("❌ Failed to trigger Jenkins build")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
