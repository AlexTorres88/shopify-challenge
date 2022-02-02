# shopify-challenge
An image repository done for the Shopify 2022 Challenge. This was for the backend summer intern position but I added a small frontend so anyone could easily test it. 

# How does it work

Basically, when a user registers in the webapp and then logs in, the application creates a bucket for them on the AWS S3 and then each user can upload, download or delete from their personal bucket. 

# Setup

For this project, you will need an AWS account and a user that is not the root user of your AWS organization.

You will also need a PostgreSQL db and you'll need to create the schema that's available at schema.txt (I know this may not be the best practice but since it's just a personal project I decided to leave it like that).  

Once you have the PostgreSQL db created, pass the connection string into the SQLALCHEMY_DATABASE_URI variable. 

The connection may look like this:

`````
SQLALCHEMY_DATABASE_URI="postgresql://[server_user]@[server_name]:[password]@[host]/[db_name]"
``````

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
