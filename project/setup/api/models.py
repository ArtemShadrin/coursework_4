from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Кристофер Нолан'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Интерстллар'),
    'description': fields.String(),
    'trailer': fields.String(),
    'year': fields.String(),
    'rating': fields.String(),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='tratata@mail.ru'),
    'password': fields.String(),
    'name': fields.String(),
    'surname': fields.String(),
    'genre': fields.Nested(genre)
})

auth: Model = api.model('Регистрация', {
    'email': fields.String(required=True, max_length=100, example='tratata@mail.ru'),
    'password': fields.String(),
})

tokens: Model = api.model('Токены', {
    'access_token': fields.String(),
    'refresh_token': fields.String(),
})
