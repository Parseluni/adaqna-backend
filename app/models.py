from app import db
from sqlalchemy.orm import relationship


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.Date)
    # parent to questions
    questions = relationship("Question", backref="question", lazy=True)
    # parent to answers
    answers = relationship("Answers", backref="answers", lazy=True)
    # parent to comments
    comments = relationship("Comment", backref="comment", lazy=True)
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "location": self.location,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    topic = db.Column(db.String)
    upvotes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # parent to answers
    answers = relationship("Answer", backref="answer", lazy=True)

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "body": self.body,
            "topic": self.topic,
            "upvotes": self.upvotes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    upvotes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # child to question
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    # parent to comments
    comments = relationship("Comment", backref="comment", lazy=True)

    def to_dict(self):
        return {
            "answer_id": self.answer_id,
            "body": self.body,
            "upvotes": self.upvotes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    upvotes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.Date)
    # child to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # child to answer
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.answer_id'))
    
    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "body": self.body,
            "upvotes": self.upvotes,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }