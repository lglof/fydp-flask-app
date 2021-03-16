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

- to install all at once `pip install -r requirements.txt`

# Running

## Basic Set Up

- Clone repo
- `cd` into repo
- Set up virtual environment `python3 -m venv venv`
- Activate the venv `source <path_to>/venv/bin/activate`
- Make sure you have all the dependencies installed
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

If you want the prepopulated db (to be used for user testing for now), update `SQLALCHEMY_DATABASE_URI` in `config.py` to `os.path.join(basedir, 'db/SOAR_testData.db')` instead of just `SOAR.db`. 

## A good testing method

In this house we love [postman](https://www.postman.com). You can run the app and then interact with it using each of the routes from within postman.

I've started using [robot framework](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variables) to make unit tests for the thing. If you want to run those, use the command `robot tests/ -d tests/reports` from the root dir of the project. These will output a bunch of things to your terminal, and you should be able to test using mostly that. But if you need more information, they also create 3 reports files, `output.xml`, `log.html`, and `report.html`. The `log.html` is really darn good. By default these are made in the root of the project, and you can update that by running `export ROBOT_OPTIONS="--outputdir tests/reports"` in your terminal. (I'm still looking for a way to set this permanently)

# Routes

## Done

### createEntry

- POST requests
- provide it with json payload containing:
  - `type` - the intervention type (string)
  - `late` - 0/1 based on not late/late intervention
  - `time` - date in the format 'YYYY-MM-DD HH:MM:SS'
  - `patient_id` - id of patient intervention performed on
  - `worker` - who performed the intervention (string)
  - `direction` - which direction the intervention was in (string)
  - `pain_level` - the patient's pain level (int)
  - `intervention_location` - where intervention was done
  - `pain_location` - where pain is
  - `pu_concern` - 0/1 based on not concerend/ concerned

```
{
    "type": 5,
    "late": 0, 
    "time": "2020-04-11 16:12:00",
    "patient_id": 1,
    "worker": "2",
    "direction": "Right",
    "painLevel": 3,
    "intervention_location": "right arm",
    "pain_location": "left leg",
    "pu_concern": 0
}
```

### getEntries/\<num>/\<id>

- GET requests
- returns the provided number of most recent interventions performed on specific patient id as a dict

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

### addDemographics
- POST requests
- provide with payload containing:
  - `age` - an integer
  - `braden_score` - an integer
  - `diagnoses` - a string with diagnoses seperated by a semicolon(;)
  - `medications` - similar to diagnoses
  - `prevention_plan` - also similar to diagnoses
  - `most_recent` - string describing the most recent intervention
  - `patient` - name of the patient impacted
  - `room` - 'Room #'
  - `mins_since_last` - the number of minutes since the last intervention
    - ideally will update this one to take time since the last intervention in a table
- creates the patient's demographics for use on overview and demographics pgs

### getDemographics/\<id>
- GET requests
- returns JSON containing demographics for patient w/ provided ID

### batchDemographics/\<num>
- GET requests
- returns JSON containing demographics for `num` patients with the longest time since the last intervention

## Working On

### filterTime

- to return interventions performed in a specified time period

### filterType/\<type>

- to return performed interventions of a certain type

### edit/\<id>

- to edit input interventions
