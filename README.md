# Longevity Interview Exercise

## Description
This project demonstrates the parsing of user supplied data via file upload and RESTful communication of Gadget and IoT devices to backend service.

### How it works 
The project enables user to upload a **CSV** file from their mobile or desktop devices.

The project also allow an electronic device to independenlty communicated with a backend sever using a recognicezed authentication key.

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
blood_type, blood_rhd`. An example CSV file can be found [here](test_data/blood_test.csv)

### Testing the API endpoint 
Using an API development tool such as Postman, make a post request to the endpoint `localhost:8000/entry-gadget/`, the API request should contain the following ` blood_pressure, 
blood_type, blood_rhd` with an Authorized bearer token. An authorized bearer token will be generated once you signup.

Each user has a unique **Authorization Token**, login as an admin to view token for each user user.

## Note
This project is not production worthy and it is only available for testing purpose only
