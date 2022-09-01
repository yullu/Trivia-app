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
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://postgres:master1*@{}/{}'.format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {"question": "Which is SA located in africa?", "answer": "South of africa Continent", "category": 5,"difficulty": 4}


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #test for creating questions
    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["questions"]))

    # Delete questions with id 4
    def test_delete_questions(self):
        res = self.client().delete("/questions/4")
        data = json.loads(res.data)

        questions = Question.query.filter(Question.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 4)
    
    # test detele a questions with a id that is not exist anywhere with ID 234
    def test_delete_question_404(self):
        response = self.client().delete('/questions/234')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    # test if question does not exist with ID 1002
    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1002")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

     # test update questions records

    def test_update_questions(self):
        res = self.client().patch("/questions/5")
        data = json.loads(res.data)
        questions = Question.query.filter(Question.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test if delete fails to delete record with error expected
    def test_400_for_failed_update(self):
        res = self.client().delete("/questions/500")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    #test quiz if running
    def starting_quiz(self)
        res = self.client().post("/quizes")
        data = json.load(res.data)

        questions = Question.query.filter(Question.id.notin_(previous_questions), 
                Question.category == category_id).all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_if_quizes_does_not_exists(self)
        res = self.client().get('/quizes')
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'inprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()