from .models import Person, Question
from ariadne import convert_kwargs_to_snake_case


### PERSON QUERIES ###

def listPersons_resolver(obj, info):
    try:
        persons = [person.to_dict() for person in Person.query.all()]
        print(persons)
        payload = {
            "success": True,
            "persons": persons
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getPerson_resolver(obj, info, person_id):
    try:
        person = Person.query.get(person_id)
        print(person)
        payload = {
            "success": True,
            "person": person.to_dict()
        }
    except AttributeError:  
        payload = {
            "success": False,
            "errors": ["Post item matching {person_id} not found"]
        }
    return payload


### QUESTION QUERIES ###

def listQuestions_resolver(obj, info):
    try:
        questions = [question.to_dict() for question in Question.query.all()]
        print(questions)
        payload = {
            "success": True,
            "questions": questions
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getQuestion_resolver(obj, info, question_id):
    try:
        question = Question.query.get(question_id)
        print(question)
        payload = {
            "success": True,
            "question": question.to_dict()
        }
    except AttributeError:  
        payload = {
            "success": False,
            "errors": ["Post item matching {question_id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def getQuestionFromPerson_resolver(obj, info, person_id, question_id):
    try:
        question = Question.query.get(question_id)
        print(question)
        payload = {
            "success": True,
            "question": question.to_dict()
        }
    except AttributeError:  
        payload = {
            "success": False,
            "errors": ["Post item matching {question_id} not found"]
        }
    return payload