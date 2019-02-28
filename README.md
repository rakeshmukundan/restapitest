# README

Swagger pets endpoint testing

## Installation

Create and activate a virtualenvironment

```
virtualenv .env
source .env/bin/activate
```

Install all the dependencies using pip.

```
pip install -r requirements.txt
```

## Configure

First, create two pet entries and note down its IDs. This is to be handled by test initiation scripts. 

Open the testconfig.ini and configure the baseurl and API KEY

Also, edit petIDtoGet and petIDtoDelete with ids of entries created

```
baseurl = https://petstore.swagger.io/v2
apikey = special-key
petIDtoGet = 6876059064504312347
petIDtoDelete = 6876059064504312344

```

# Run

All tests can be executed by running

```
make run
```

# Results

Results will be stored in a file named results.html in the same directory. It can be opened in a browser to view results and logs

