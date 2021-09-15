# shopify-challenge
An image repository done for the Shopify 2022 Challenge

# Setup

For this setup, you will need an AWS account, a user that is not the root user of your organization and have a bucket created.

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