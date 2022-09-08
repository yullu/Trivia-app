import os
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def pagination_questions(requests, selections):
  pages = requests.args.get('page', 1, type=int)
  start = (pages-1) * QUESTIONS_PER_PAGE
  end = start+QUESTIONS_PER_PAGE

  questions = [question.format() for question in selections]
  current_questions = questions[start:end]

  return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    CORS(app, resources={r"/api/*": {"origins": "*"}})
    

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    @app.route('/categories')
    def get_categories():

        categories = {category.id: category.type for category in Category.query.all()}

        return jsonify(
            {
                'success': True,
                'categories': categories,
                'total_categories': len(categories)
            }
        )


    @app.route('/questions')
    def list_questions():
       
        listing = Question.query.all()
        current_questions = pagination_questions(request, listing)
        output = {category.id: category.type for category in Category.query.all()}

        
        return jsonify({
            'success':True,
            'questions':current_questions,
            'total_questions' : len(listing),
            'categories': output,
            })


    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def deleting_question(question_id):
            questions_name= Question.query.get(question_id)
           
            if (questions_name == 0):
                abort(404)

            else:
            
                question_names.delete()

                total_questions_remaining = len(Question.query.all())

                return jsonify({
                'success': True,
                'deleted': question_id,
                'total_questions': total_questions_remaining
                })

    @app.route('/questions', methods=['POST'])
    def add_new_question():

        new_data = request.get_json()

        add_question = new_data['question']
        add_answer = new_data['answer']
        add_category = new_data['category']
        add_difficulty = new_data['difficulty']

        if(request.new_data == 0):
            abort(422)

        else:
            responses = Question(
                question=add_question,
                answer=add_answer,
                category=add_category,
                difficulty=add_difficulty
                )

            responses.insert()

            tot_questions = Question.query.all()
            current_questions = pagination_questions(request, tot_questions)

            return jsonify({
            'success': True,
            'created': question.id,
            'questions': current_questions,
            'total_questions': len(tot_questions)
        })
       

    @app.route('/questions/search', methods=['POST'])
    def searching_question():
        searching = request.get_json()
        searchTerm = searching.get('searchTerm')

        try:
            search_results= Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm)))
            tot_questions = Question.query.all()
            current_question = pagination_questions(request, search_results)

            return jsonify({
                'success': True,
                'questions': current_question,
                'total_questions': len(search_results.all()),
                
            })

        except Exception:
            abort(400)

    @app.route('/categories/<int:category_id>/questions')
    def get_category_question(category_id):

        try:
            listing = Question.query.filter(category_id == Question.category).all()
    
            current_questions = pagination_questions(request, listing)
            categories = Category.query.all()
            curent_category = {category.type for category in Category.query.filter(Category.category.id == category_id).all()}

            if category_id > len(categories):
                abort(404)
            else:

                return jsonify({
                    "success": True,
                    "questions": list(current_questions),
                    "total_questions": len(listing),
                    "current_category": curent_category
                })
        except:
            abort(404)
        

    @app.route('/quizzes', methods=['POST'])
    def engage_quiz():
        try:
            eric = request.get_json()
            get_quiz_category = eric.get('quiz_category')
            get_previous_questions = eric.get('previous_questions')
            get_category_id = get_quiz_category['id']
            previous_questions_size = len(get_previous_questions)

            if get_category_id == 0 & previous_questions_size == 0:
                questions = Question.query.order_by(Question.id).all()
            elif get_category_id == 0 & previous_questions_size > 0:
                questions = Question.query.filter(
                    Question.id.notin_(get_previous_questions)).all()
            else:
                questions = Question.query.filter(Question.id.not_in(get_previous_questions),
                                                  Question.category == get_category_id).all()
            
            question = None
            if (questions):
                question = random.choice(questions)

            return jsonify({
                'success': True,
                'question': question.format()
            })
        except:
            abort(422)
        


    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
          'success': False, 
          'error': 404,
          'message': 'resource not found'
        }), 404
    
    @app.errorhandler(422)
    def unprocessible_error(error):
        return jsonify({
          'success': False, 
          'error': 422,
          'message': 'unprocessible'
        }), 422

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({
          'success': False,
          'error': 400,
          'message': 'bad request'
        }), 400


    @app.errorhandler(405)
    def not_allowed_request_error(error):
        return jsonify({
          'success': False,
          'error': 405,
          'message': 'method not allowed'
        }), 405


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
          'success': False, 
          'error': 500, 
          'message': 'internal server error'
        }), 500

    return app