# ToC:

1. Dependencies
2. Running
   1. Set up
   2. Basic db functions
   3. Running the app
   4. Suggested testing methods
3. Routes

# Dependencies:

- Flask, migrate, and SQLAlchemy `pip install Flask Flask-Migrate Flask-SQLAlchemy`
- sqlite `apt install sqlite3`

# Running

## Basic Set Up

- Clone repo
- `cd` into repo
- Set up virtual environment `python3 -m venv venv`
- Activate the venv `source <path_to>/venv`
- Make sure you have all the dependencies installed
- To get the db going `Flask db upgrade`
  - _I'm not sure if this part is right_
- Then to finally run the app `Flask run`

## Basic Db Functions

_This is for interactions with the db structure._

Make changes to db structure inside the `src/models.py` file.
Then run `Flask db migrate -m 'your message'` -> this makes a migration record with the attached message (we love human readability).
Double check that the changes were correct.
If they _weren't correct_ just delete the generated file (it's in `migrations/`).
If they _were correct_ run `Flask db upgrade` and watch your changes be implemented!

To interact with the db directly (I'll do this to just manually make sure things are updating) you can run `sqlite3 <path_to>/SOAR.db` and then use basic SQL queries to interact.

## Running the App

You'll be running with the `Flask run` command. If you want the server to notice any changes you make to a `.py` file and update to new code you can set an environment variable. `export FLASK_DEBUG=1`

## A good testing method

In this house we love [postman](https://www.postman.com). You can run the app and then interact with it using each of the routes from within postman.

# Routes

## Done

### createEntry

- POST requests
- provide it with json payload containing:
  - `type` - the intervention type (string)
  - `worker` - who performed the intervention (string)
  - `direction` - which direction the intervention was in (string)
  - `pain_level` - the patient's pain level (int)

### getEntries/\<num>

- GET requests
- returns the provided number of most recent interventions as a dict

```
{
    'items': [{intervention_data}, {intervention_data}]
}
```

### deleteEntry/\<id>

- DELETE requests
- deletes the entry with the provided id

### verify

- GET requests
- provide it with json payload containing:
  - `friendly` - the username (string)
  - `password` - plaintext password (string)
- returns `{"check": True/False}` based on whether the password is correct or incorrect

### newUser/\<userType>

- POST requests
- provide with a json payload containing:
  - `friendly` - the username (string)
  - `password` - plaintext password (string)
- creates a user with the provided friendly name, password, and user type

### deleteUser/\<id>

- DELETE requests
- deletes the user with the provided id

## Working On

### filterTime

- to return interventions performed in a specified time period

### filterType/\<type>

- to return performed interventions of a certain type

### edit/\<id>

- to edit input interventions
