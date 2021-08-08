import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor, db


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the CastingAgency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "CastingAgency"  # _test"

        setup_db(self.app)
        db.create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_delete_actor(self):
        response = self.client().delete('/actors/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], id)

    def test_405_if_actor_deletion_not_allowed(self):
        response = self.client().delete('/actors/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_delete_movie(self):
        response = self.client().delete('/movies/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], id)

    def test_405_if_movie_deletion_not_allowed(self):
        response = self.client().delete('/movies/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_post_actor(self):
        response = self.client().post('/actors/new')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_if_actor_creation_not_allowed(self):
        response = self.client().post('/actors/new')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_post_movie(self):
        response = self.client().post('/movies/new')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_405_if_movie_creation_not_allowed(self):
        response = self.client().post('/movies/new')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_actor(self):
        response = self.client().patch('actors/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_if_actor_update_not_allowed(self):
        response = self.client().patch('/actors/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_movie(self):
        response = self.client().patch('movies/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_405_if_movie_update_not_allowed(self):
        response = self.client().patch('/movies/<id>')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
