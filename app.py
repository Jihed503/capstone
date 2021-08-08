import os
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import *
from auth import AuthError, requires_auth
from flask_migrate import Migrate

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    setup_db(app)
    CORS(app)

    db_drop_and_create_all()

    # Set Access-Control-Allow

    @app.after_request
    def after_request_func(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTION')
        return response

    # Routes

    def index():
        return jsonify({
            'message': 'Welcome to My api_name'
        })

    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = [actor.format() for actor in Actor.query.all()]
        return jsonify({
            'actors': actors,
            'success': True,
        }), 200

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = [movie.format() for movie in Movie.query.all()]
        return jsonify({
            'movies': movies,
            'success': True,
        }), 200

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(id):

        actor_to_delete = Actor.query.filter(Actor.id == id)

        if actor_to_delete is None:
            abort(404)

        try:
            actor_to_delete.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        except exc.SQLAlchemyError:
            abort(503)
            db.session.rollback()
        except Exception:
            abort(422)
            db.session.rollback()

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(id):

        movie_to_delete = Movie.query.filter(Movie.id == id).one_or_none()

        if movie_to_delete is None:
            abort(404)

        try:
            movie_to_delete.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        except exc.SQLAlchemyError:
            abort(503)
            db.session.rollback()
        except Exception:
            abort(422)
            db.session.rollback()

    @app.route('/actors/new', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):
        try:
            new_actor = Actor(name=json.loads(
                                  request.data.decode('utf-8')
                                  )['name'],
                              age=json.loads(
                                  request.data.decode('utf-8'))['age'],
                              gender=json.loads(
                                  request.data.decode('utf-8'))['gender'],
                              movie_id=json.loads(
                                  request.data.decode('utf-8')
                                  )['movie_id'])
            Actor.insert(new_actor)
            actor = [new_actor.format()]

            return jsonify({
                "success": True,
                "actors": actor
            }), 200
        except exc.SQLAlchemyError:
            print(sys.exc_info())
            abort(422)
            db.session.rollback()
        except Exception:
            abort(503)
            db.session.rollback()

    @app.route('/movies/new', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
        try:
            new_movie = Movie(title=json.loads(
                                request.data.decode('utf-8')
                                )['title'],
                              release_date=json.loads(
                                  request.data.decode('utf-8')
                                  )['release_date'])
            Movie.insert(new_movie)
            movie = [new_movie.format()]

            return jsonify({
                "success": True,
                "movies": movie
            }), 200
        except exc.SQLAlchemyError:
            print(sys.exc_info())
            abort(422)
            db.session.rollback()
        except Exception:
            abort(503)
            db.session.rollback()

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(payload, id):
        try:
            actor_to_update = Actor.query.filter(id == id)

            name = request.get_json().get('name')
            actor_to_update.name = name

            age = request.get_json().get('age')
            actor_to_update.age = age

            gender = request.get_json().get('gender')
            actor_to_update.gender = gender

            movie_id = request.get_json().get('movie_id')
            actor_to_update.movie_id = movie_id

            actor_to_update.update()
            actor = [actor_to_update.format()]

            return jsonify({
                "success": True,
                "actors": actor
            }), 200
        except Exception:
            abort(404)
            db.session.rollback()
        except exc.SQLAlchemyError:
            abort(422)
            db.session.rollback()

    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(payload, id):
        try:
            movie_to_update = Movie.query.filter(id == id)

            title = request.get_json().get('title')
            movie_to_update.title = title

            release_date = request.get_json().get('release_date')
            movie_to_update.release_date = release_date

            movie_to_update.update()
            movie = [movie_to_update.format()]

            return jsonify({
                "success": True,
                "movies": movie
            }), 200
        except Exception:
            abort(404)
            db.session.rollback()
        except exc.SQLAlchemyError:
            abort(422)
            db.session.rollback()

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resources Not Found'
        }), 404

    @ app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
