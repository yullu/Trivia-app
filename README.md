# Trvia App Gaming APi Documentation

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

All backend code follows PEP8 style guidelines.

## Getting Started

## Pre-requisites and Local Development
For Developers to effectively use run and use this project should already have Python3, pip and node installed on your local machine.


### Backend and run the backend server

From the backend folder run pip install requirements.txt. All required packages are included in the requirements file.

These commands put the application in development and directs our application to use the __init__.py file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

### Frontend install and run frontend server

From the frontend folder, run the following commands to start the client:

npm install // only once to install dependencies
npm start //to start the server after installation of dependancies

By default, the frontend will run on localhost:3000.


## API Reference
### Getting started with API
Base URL: Currently this application is only for hosted locally application. The backend is url is http://127.0.0.1:5000/ Authentication: This version does not require authentication or API keys.

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

## Endpoints
### Get/categories
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


## Author
The App has been modified by Eric Yullu

## Acknowledgements

Most important aknowledgement goes to Udacity team ans especially our session lead for best hand held and guidance for success of this program.