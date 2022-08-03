# Longevity Interview Exercise

## Description
This exercise comprises of two seperate cards, 
This project demonstrates the parsing of user supplied data via file upload, RESTful communication of Gadget and IoT devices to backend service and Rewarding user for performing a specific task.

### How File Upload Section Works
The project enables user to upload a **CSV** file from their mobile or desktop devices.

The project also allow an electronic device to independenlty communicated with a backend sever using a recognicezed authentication key.

Code for user entry via form input can be found here [here](user_input/)
Code for user entry via tracker app is available here [here](tracker_entry/)
### How User Rewarding Works

The second part of this project works by rewarding user's with $LONG Token for completing a task, task are created when the user signs up and the users are awarded the moment they complete a specific task.

The second project folder can be found [here](reward/)
## Dependencies
### Major Dependencies
This project was tested on a Debian 11 environment with the following packages installed:
```
Python 3.9
Django 4.0.6
PostgreSQL 13
```
### Minor Dependencies
The project depends on the following python libraries
```
asgiref==3.5.2
autopep8==1.6.0
certifi==2022.6.15
cffi==1.15.1
charset-normalizer==2.1.0
cryptography==37.0.4
defusedxml==0.7.1
Django==4.0.6
django-allauth==0.51.0
djangorestframework==3.13.1
idna==3.3
numpy==1.23.1
oauthlib==3.2.0
pandas==1.4.3
Pillow==9.2.0
psycopg2-binary==2.9.3
pycodestyle==2.8.0
pycparser==2.21
PyJWT==2.4.0
python-dateutil==2.8.2
python3-openid==3.2.0
pytz==2022.1
requests==2.28.1
requests-oauthlib==1.3.1
six==1.16.0
sqlparse==0.4.2
toml==0.10.2
urllib3==1.26.10
```
## Running the project
1. Clone or Download the repository
2. Change to the base directory of the clonned or downloaded project using any terminal of your choice
3. Build a docker image by running the command `docker-compose up ` 
4. Open your web browser and navigate to `localhost:8000`
5. Login with the default username **Ruby** and password **ruby**
6. Upload a CSV file with the following coloum names ` blood_pressure, 
blood_type, blood_rhd`. An example CSV file can be found [here](test_data/test_file.csv)

### Testing the API endpoint 
Using an API development tool such as Postman, make a post request to the endpoint `localhost:8000/entry-gadget/`, the API request should contain the following ` blood_pressure, 
blood_type, blood_rhd` with an Authorized bearer token. An authorized bearer token will be generated once you signup.

Each user has a unique **Authorization Token**, login as an admin to view token for each user user.

#### cURL command to test the API

The cURL command below describes an example of the API call
```shell
curl --location --request POST '127.0.0.1:8000/entry-gadget/' \
--header 'Authorization: Bearer e829b78e3319d4a9273831ef43242c987a62910c' \
--form 'input_file=@"/absolute/path/of/project/test_data/blood_test.csv"' \
--form 'file_ext="csv"'
```
#### Python code to test the API
The code below shows an API request using python
```python
import requests

url = "127.0.0.1:8000/entry-gadget/"

payload={'file_ext': 'csv'}
files=[
  ('input_file',('blood_test.csv',open('/absolute/path/of/project/test_data/blood_test.csv','rb'),'text/csv'))
]
headers = {
  'Authorization': 'Bearer e829b78e3319d4a9273831ef43242c987a62910c'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```
`e829b78e3319d4a9273831ef43242c987a62910c` is the Authentication token and it is unique for each user.

## Known Issue
1. Requesting for credentials of an insecure request is prohibited by most providers, the **Import Data From Google Fit App** is a demo of how fitness app import could be implemented.
2. A strict check was not employed on rewarding system, which means a user can be rewarded several times for performing same task.
For instance, a user will be rewarded for linking a device or app, and the user decided to remove the app, this user will be rewarded when they link same app again. This issue can be fixed by assigning a inique properties to a completed task which could make the task impossible to retake. 
3. For the sake of simplicity of this testing, mailing feature was not included and codes were not splitted in chunks.

## Note
1. This project is not production worthy and it is only available for testing purpose only
2. While I have included google authentication credentials for testing, feel free to overwrite the existing credentials
3. The following links should be used while setting up your own GCP project, please follow [this guide](https://developers.google.com/identity/protocols/oauth2/web-server) for setting up you own GCP app.


