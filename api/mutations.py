from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Person, Question


### PERSON MUTATIONS ###
@convert_kwargs_to_snake_case
def create_person_resolver(obj, info, username, email, location):
    try:
        today = date.today()
        person = Person(
            username=username, email=email, location=location, created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(person)
        db.session.commit()
        payload = {
            "success": True,
            "person": person.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_person_resolver(obj, info, person_id, username, email, location):
    try:
        person = Person.query.get(person_id)
        if person:
            person.username = username
            person.email = email
            person.location = location
        db.session.add(person)
        db.session.commit()
        payload = {
            "success": True,
            "person": person.to_dict()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": ["item matching id {person_id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_person_resolver(obj, info, person_id):
    try:
        person = Person.query.get(person_id)
        db.session.delete(person)
        db.session.commit()
        payload = {
            "success": True, "person": person.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload


### QUESTION MUTATIONS ###

@convert_kwargs_to_snake_case
def create_question_resolver(obj, info, person, body, topic):
    try:
        today = date.today()
        question = Question(
            person=Person.person_id, body=body, topic=topic, created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(question)
        db.session.commit()
        payload = {
            "success": True,
            "question": question.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_question_resolver(obj, info, question_id, body, topic):
    try:
        question = Question.query.get(question_id)
        if question:
            question.body = body
            question.topic = topic
        db.session.add(question)
        db.session.commit()
        payload = {
            "success": True,
            "question": question.to_dict()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": ["item matching id {question_id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_question_resolver(obj, info, question_id):
    try:
        question = Question.query.get(question_id)
        db.session.delete(question)
        db.session.commit()
        payload = {
            "success": True, "question": question.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload