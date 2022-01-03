from api import db
from sqlalchemy.orm import relationship


class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    location = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.Date)
    # parent to questions
    questions = relationship("Question", backref="question", lazy=True)
    # parent to answers
    answers = relationship("Answers", backref="answers", lazy=True)
    # parent to comments
    comments = relationship("Comment", backref="comment", lazy=True)
    
    def to_dict(self):
        return {
            "person_id": self.person_id,
            "username": self.username,
            "email": self.email,
            "location": self.location,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    topic = db.Column(db.String)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to person
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    # parent to answers
    answers = relationship("Answer", backref="answer", lazy=True)

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "body": self.body,
            "topic": self.topic,
            "votes": self.votes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to person
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    # child to question
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    # parent to comments
    comments = relationship("Comment", backref="comment", lazy=True)

    def to_dict(self):
        return {
            "answer_id": self.answer_id,
            "body": self.body,
            "votes": self.votes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to person
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    # child to answer
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.answer_id'))
    
    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "body": self.body,
            "votes": self.votes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
        