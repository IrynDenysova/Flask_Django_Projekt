# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from app.extentions import db, migrate
from app.models.response import Response
from app.models.questions import Question, Statistic
from app.models.category import Category

__all__ = [
    'Question',
    'Statistic',
    'Response',
    'Category',
]
