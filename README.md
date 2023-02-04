# OpenAI API Quickstart - Python example app

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Next steps to add the variables to the newly created `.env` file
8. Add your [API key](https://beta.openai.com/account/api-keys)  for the variable OPENAI_API_KEY
9. Add your google cloud project name for variable GOOGLE_PROJECT_ID
10. Create and Download your google cloud project's [service account](https://cloud.google.com/iam/docs/service-accounts) using the steps
11. Copy the service account JSON file content to static/service_account.json

12. Run the app

    ```bash
    $ flask run
    ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
