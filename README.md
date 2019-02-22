# Stackery CRUD Demo - Python 2.7

This is a sample template for a serverless AWS Lambda application, written in Python.

The application implements a CRUD interface in front of an AWS DynamoDB table that
manages a simple user record.  An API Gateway distributes requests to the various
AWS Lambda functions based on their HTTP paths and methods.

The application architecture is defined in template.yaml, a Serverless
Application Model (SAM) template which can be managed through the Stackery UI
at app.stackery.io.

Here is an overview of the files:

```text
.
├── README.md                          <-- This README file
├── src                                <-- Source code dir for all AWS Lambda functions
│   ├── createUser                     <-- Source code dir for createUser function
│   │   ├── requirements.txt           <-- Build dependencies for createUser
│   |   └── handler.py                 <-- Lambda createUser function code 
│   ├── getUser                        <-- Source code dir for getUser function
│   │   ├── requirements.txt           <-- Build dependencies for getUser
│   |   └── handler.py                 <-- Lambda getUser function code 
│   ├── updateUser                     <-- Source code dir for updateUser function
│   │   ├── requirements.txt           <-- Build dependencies for updateUser
│   |   └── handler.py                 <-- Lambda updateUser function code 
│   ├── deleteUser                     <-- Source code dir for deleteUser function
│   │   ├── requirements.txt           <-- Build dependencies for deleteUser
│   |   └── handler.py                 <-- Lambda deleteUser function code 
│   └── listUsers                      <-- Source code dir for listUsers function
│   │   ├── requirements.txt           <-- Build dependencies for listUsers
│   |   └── handler.py                 <-- Lambda deleteUser function code listUsers
└── template.yaml                      <-- SAM infrastructure-as-code template
```

Clone this stack in Stackery, deploy it, and test as follows:

- Set `STAGE_LOCATION` from the deployed Rest Api resource properties.

- Create a user:

        curl --header "Content-Type: application/json" \
        --request POST \
        --data '{"id": "unique001", "firstName": "Alice", "lastName": "Smith", "color": "blue"}' \
        ${STAGE_LOCATION}/users

- List users:

        curl ${STAGE_LOCATION}/users

- Read a user:

        curl ${STAGE_LOCATION}/users/unique001

- Update a user:

        curl --header "Content-Type: application/json" \
        --request PUT \
        --data '{"firstName": "Alice", "lastName": "Smith", "color": "green"}' \
        ${STAGE_LOCATION}/users/unique001

- Delete a user:

        curl --request DELETE ${STAGE_LOCATION}/users/unique001
