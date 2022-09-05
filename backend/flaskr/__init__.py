import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def pagination_questions(request, selections):
  page = request.args.get('page', 1, type=int)
  start = (page-1) * QUESTIONS_PER_PAGE
  end = start+QUESTIONS_PER_PAGE

  questions = [question.format() for question in selections]
  current_questions = questions[start:end]

  return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories', methods=['GET'])
    def retrieve_categories():
        category = Category.query.order_by(Category.id).all()
        current_category = pagination_questions(request, category)

        category = {category.id:category.type for category in category}

        if len(current_category) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': category,
            "total_categories": len(Category.query.all())
        })

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions', methods=['GET'])
    def list_questions():
       
        listing = Question.query.order_by(Question.id).all()
        current_questions = pagination_questions(request, listing)
        categories = Category.query.order_by(Category.type).all()

        category = {category.id: category.type for category in categories}

        if(len(current_questions)==0):
         abort(404)
        
        return jsonify({
            'success':True,
            'questions':current_questions,
            'total_questions' : len(listing),
            'categories': category,
            'current_category': None
            })
    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            quest = Question.query.get(question_id)
            question_name= Question.query.get(question_id)
           
            
            if quest is None:
                abort(404)
            
            quest.delete()

            total_questions = len(Question.query.all())

            return jsonify({
                'success': True,
                'deleted': question_id,
                'total_questions': total_questions
            })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def add_question():

        body = request.get_json()

        new_question = body.get('question')
        new_answer = body.get('answer')
        new_category = body.get('category')
        new_difficulty = body.get('difficulty')

        #chekin to ensure all fields are not empty
        if (body, new_question, new_answer, new_category, new_difficulty) == None:
            abort(422)

        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty
                )

            question.insert()

            tot_questions = Question.query.all()
            current_questions = pagination_questions(request, tot_questions)

            return jsonify({
            'success': True,
            'created': question.id,
            'questions': current_questions,
            # 'created': question.new_question,
            'total_questions': len(tot_questions)
        })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new category,
    which will require the type for the category 
    TEST: When you submit a cagory on the "Cat" tab,
    the form will clear and the question will appear at the end of the last page
    of the Category list
    """
    @app.route('/categories', methods=['POST'])
    def add_category():

        #body = request.get_json()
        json_data = request.get_json()

        new_category = json_data.get('type')

        #chekin to ensure all fields are not empty
        if (new_category) == None:
            abort(422)

        try:
            category = Category(type=new_category)

            category.insert()

            tot_category = Category.query.all()
            #current_questions = pagination_questions(request, tot_questions)

            return jsonify({
            'success': True,
            'created': category.id,
            #'questions': current_questions,
            # 'created': question.new_question,
            'tot_category': len(tot_category)
        })
        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.
    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_question():
        body = request.get_json()
        searchTerm = body.get('searchTerm', None)

        try:
            results= Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(searchTerm)))
            tot_questions = Question.query.all()
            current_question = pagination_questions(request, results)

            #category = {category.id:category.type for category in category}


            return jsonify({
                'success': True,
                'questions': current_question,
                'total_questions': len(results.all()),
                #'current_category': category
                
            })

        except Exception:
            abort(400)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions')
    def category_question(category_id):

        try:
            listing = Question.query.filter(category_id == Question.category).all()
    
            current_questions = pagination_questions(request, listing)
            categories = Category.query.all()

            if category_id > len(categories):
                abort(404)

            return jsonify({
                    "success": True,
                    "questions": list(current_questions),
                    "total_questions": len(listing),
                    "current_category": [category.type for category in categories if category.id == category_id ]
                })
        except:
            abort(404)
        
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def engage_quiz():
        try:
            obtain = request.get_json()
            quiz_category = obtain.get('quiz_category')
            previous_questions = obtain.get('previous_questions')
            category_id = quiz_category['id']

            if (category_id == 0):
                questions = Question.query.all()
            else:
                questions = Question.query.filter(Question.category == category_id).all()
            question = None
            if(questions):
                question = random.choice(questions)

            return jsonify({
                'success': True,
                'question': question.format()
            })
        except:
            abort(422)




    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          'success': False, 
          'error': 404,
          'message': 'resource not found'
        }), 404
    
    @app.errorhandler(422)
    def unprocessible(error):
        return jsonify({
          'success': False, 
          'error': 422,
          'message': 'unprocessible'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          'success': False,
          'error': 400,
          'message': 'bad request'
        }), 400


    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
          'success': False,
          'error': 405,
          'message': 'method not allowed'
        }), 405


    @app.errorhandler(500)
    def internal_server(error):
        return jsonify({
          'success': False, 
          'error': 500, 
          'message': 'internal server error'
        }), 500

    return app