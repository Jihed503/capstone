# Full Stack Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Heroku link: https://castingfsndagency.herokuapp.com/
Heroku git URL: https://git.heroku.com/castingfsndagency.git
DATABASE_URL: postgres://guzemgdwldzpsm:43d9f428fb3828c1c1f1cbb37b5745250a1a157c462ffb425b486880b35698f9@ec2-50-16-198-4.compute-1.amazonaws.com:5432/ddfdg9qoer2t53

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### Installing virtualenv

- On macOS and Linux:

  ```
  python3 -m pip install --user virtualenv
  ```

- On Windows:

  ```
  py -m pip install --user virtualenv
  ```

##### Creating a virtual environment

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

- On macOS and Linux:

  ```
  python3 -m venv env
  ```

- On Windows:

  ```
  py -m venv env
  ```

##### Activating a virtual environment

- On macOS and Linux:

  ```
  source env/bin/activate
  ```

- On Windows:

  ```
  .\env\Scripts\activate
  ```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

- On macOS and Linux:

  ```
  which python
  .../env/bin/python
  ```

- On Windows:

  ```
  where python
  .../env/bin/python.exe
  ```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

To run the server, execute:

- On Linux : export

```bash
export FLASK_APP=app.py;
export FLASK_ENV=development;
flask run;
```

- On Windows : set

```
set FLASK_APP=app.py;
set FLASK_ENV=development;
flask run;
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

## DATA MODELING:

MODELS.PY

The schema for the database and helper methods to simplify API behavior are in models.py:

- There are two tables created: Movie, Actor
- The Actor table is used by the roles 'Casting Director' and 'Executive Producer' to add, delete and modify actors.
- The Actor table has a foreign key on the Movie table for movie_id.
- The Movie table is used by the role 'Casting Director' to update movies and by the user 'Executive Producer' to add, delete and modify movies.
- Each table has an insert, update, delete, and format helper functions.

## Endpoints

GET '/actors'
GET '/movies'
DELETE '/actors/<id>'
DELETE '/movies/<id>'
POST '/actors/new'
POST '/movies/new'
PATCH '/actors/<id>'
PATCH '/movies/<id>'

GET '/actors'

- Fetches all the actors in the databse
- Request Arguments: None
- Returns: An object with two key, success, actors, that contains a list of actors.

Sample response output:

```
{
  'actors': [
    {
      'id': 1,
      'name': Omar,
      'age': 35,
      'gender': Male,
      'movie_id': 2
    },
    {
      'id': 2,
      'name': Hend,
      'age': 40,
      'gender': Female,
      'movie_id': 1
    }
  ],
  'success': True,
}
```

GET '/movies'

- Fetches all the movies in the databse
- Request Arguments: None
- Returns: An object with two key, success, movies, that contains a list of movies.

Sample response output:

```
{
  'movies': [
    {
      'id': 1,
      'title': Lockdown,
      'release_date': 27/07/2020
    },
    {
      'id': 2,
      'title': Corona,
      'release_date': 27/06/2020
    }
  ],
  'success': True,
}
```

DELETE '/actors/1'

- Deletes an actor based on id
- Request Arguments: id
- Returns: An object with two keys, success, id

Sample response output:

```
{
  'success': True,
  'delete': 1
}
```

DELETE '/movies/2'

- Deletes a movie based on id
- Request Arguments: id
- Returns: An object with two keys, success, id

Sample response output:

```
{
  'success': True,
  'delete': 2
}
```

POST '/actors/new'

- Create a new actor in the database.
- Request Arguments: None
- Returns: an object with two keys: success, actors.

Sample response output:

```
{
  "success": True,
  "actors": [
    {
      'id': 3,
      'name': Jihed,
      'age': 20,
      'gender': Male,
      'movie_id': 1
    }
  ]
}
```

POST '/movies/new'

- Create a new movie in the database.
- Request Arguments: None
- Returns: an object with two keys: success, movies.

Sample response output:

```
{
  "success": True,
  "movies": [
    {
      'id': 3,
      'title': Hope,
      'release_date': 15/03/2020
    }
  ]
}
```

PATCH '/actors/1'

- Modifies the actor based on the id.
- Request Arguments: id
- Returns: an object with two keys: success, actors.

Sample response output:

```
{
  "success": True,
  "actors": [
    {
      'id': 1,
      'name': Omar,
      'age': 25,
      'gender': Male,
      'movie_id': 2
    }
  ]
}
```

PATCH '/movies/1'

- Modifies the movie based on the id.
- Request Arguments: id
- Returns: an object with two keys: success, movies.

Sample response output:

```
{
  "success": True,
  "movies": [
    {
      'id': 1,
      'title': Lockdown,
      'release_date': 27/04/2020
    }
  ]
}
```

## Roles

- Casting Assistant

  - Can view actors and movies

- Casting Director

  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies

- Executive Producer
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database

## Testing

To run the tests, run

```
python test_app.py
```

define all the credentials in the file setup.sh so that it can be exported to that instance of terminal by running the command

```
source setup.sh
```

## Authors

Yours truly, Jihed Selmi

## Acknowledjments

The awesome team of Udacity and my colleagues
