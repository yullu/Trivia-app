# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

For Developers to effectively use run and use this project should already have Python3, pip and node installed on your local machine.

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database
With Postgres running, restore the database using the trivia.psql file provided. From the backend folder in terminal run:

psql trivia < trivia.psql

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute the following commands:

set FLASK_APP=__init__.py
set FLASK_ENV=development
flask run

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

## Documenting your Endpoints
### Error Handling

Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

{
    "success": True, 
    "error": 200,
    "message": "success"
}

The API will return five error types when requests fail:

    400: Bad Request
    404: Resource Not Found
    422: Not Processable
    405: method not allowed
    500: internal server error


### Documentation Example

- Fetches object of all categories.. 
- Sample curl: `curl http://127.0.0.1:5000/categories`
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
### Get/questions
- Returns object containing all questions that are available
- Sample of curl : `curl http://127.0.0.1:5000/questions`
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 1, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 2, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 3, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 5, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 6, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 7, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 8, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "kenyatta", 
      "category": 4, 
      "difficulty": 3, 
      "id": 34, 
      "question": "Who was the first president of kenya"
    }, 
    {
      "answer": "Bill gates", 
      "category": 1, 
      "difficulty": 1, 
      "id": 35, 
      "question": "Whos is ower od microsoft"
    }
  ], 
  "success": true, 
  "total_questions": 31
}
### Delete/questions/questions/{question_id}>
This endpint enables deletion of questions bearing the specified id

Sample curl: `curl -X DELETE http://127.0.0.1:5000/questions/3`

{
  "deleted": 3,
  "success": true,
  "total_questions": 8
}
###POST '/play'

- This endpoint enables player to play the trivia Api game

Sample curl: `curl http://127.0.0.1:5000/play -X POST -H "Content-Type: application/json" -d '{"previous_questions": [3, 4], "quiz_category": {"type": "History", "id": "4"}}'`


## Testing

def test_get_list_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['categories'])
        self.assertEqual(len(data['total_categories']))
