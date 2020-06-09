import json

from functools import wraps

from marshmallow import ValidationError
from app.api.validator.user_post_shema import EntityError

from flask import request, jsonify, g

BAD_REQUEST = 400
UNPROCESSABLE_ENTITY = 422

def validate_schema(schema):
  def wrapper(function):
      @wraps(function)
      def wrapped(*args, **kwargs):
          try:
            data = json.loads(request.data) if request.data else {}
          except ValueError:
            return jsonify(code=BAD_REQUEST, message='Invalid request body'), BAD_REQUEST
          except TypeError:
            return jsonify(code=BAD_REQUEST, message='Invalid request body'), BAD_REQUEST

          try:
            validated_params = schema.load(data)
          except ValidationError as err:
            return jsonify(code=BAD_REQUEST, message=err.messages), BAD_REQUEST
          except EntityError as err:
            return jsonify(code=UNPROCESSABLE_ENTITY, message=err.message), UNPROCESSABLE_ENTITY

          g.validated_params = validated_params
          return function(*args, **kwargs)
      return wrapped
  return wrapper
