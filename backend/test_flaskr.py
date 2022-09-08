import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = 'postgresql://postgres:master1*@{}/{}'.format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'Who was the 4th president of Kenya',
            'answer': 'Uhuru',
            'category':4,
            'difficulty': 2
        }
    
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        eri = self.client().get('/categories')
        data = json.loads(eri.data)
        self.assertEqual(eri.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))


    def test_get_questions_with_pagination(self):
        eri = self.client().get('/questions')
        data = json.loads(eri.data)
        self.assertEqual(eri.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_creating_new_questions(self):
        eri = self.client().post('/questions', json=self.new_question)
        data = json.loads(eri.data)

        self.assertEqual(eri.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_405_if_questions_not_permitted(self):
        eri = self.client().post('/questions/405', json=self.new_question)
        data = json.loads(eri.data)

        self.assertEqual(eri.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_deleting_question(self):
        eri = self.client().delete('/questions/8'):
        data = json.loads(eri.data)

        question = Question.query.filter(Question.id == 8).one_or_none()

        self.assertEqual(eri.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'], 8)

    def test_deteling_question_not_found(self):
        eri = self.client().delete('/questions/800')
        data = json.loads(eri.data)

        self.assertEqual(eri.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()