# shopify-challenge
An image repository done for the Shopify 2022 Challenge

# Setup

For this setup, you will need an AWS account, a user that is not the root user of your organization and have a bucket created.

You will also need a PostgreSQL db and you'll need to create the schema that's available at schema.txt (I know this may not be the best practice but since it's just a personal project I decided to leave it like that).  

Once you have the PostgreSQL db created, pass the connection string into the SQLALCHEMY_DATABASE_URI variable. 

The connection may look like this:

`````
SQLALCHEMY_DATABASE_URI="postgresql://[server_user]@[server_name]:[password]@[host]/[db_name]"


After that you will need to create a virtual environment:

`````
python3 -m venv [virtual_env_name]
`````

Now, we need to activate the virtual env:

`````
source [virtual_env_name]/bin/activate
`````

To deactivate, you can run:

`````
deactivate
``````

After we have our virtual environment, we can install our requirements by running:

`````
pip install -r requirements.txt
`````

All that is left to do is export the application variables and run it:

`````
export FLASK_APP=app
export FLASK_ENV=development
flask run
`````
