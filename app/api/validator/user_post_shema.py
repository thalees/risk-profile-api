from marshmallow import Schema, fields, validate, validates, ValidationError


class EntityError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class HomeSchema(Schema):
    ownership_status = fields.Str(
      required=True,
      validate=validate.OneOf(
        choices=['owned', 'mortgaged']
      )
    )


class VehicleSchema(Schema):
    year = fields.Int(required=True)


class UserPostSchema(Schema):
    age = fields.Int(required=True)

    dependents = fields.Int(required=True)

    income = fields.Int(required=True)

    marital_status = fields.Str(
      required=True,
      validate=validate.OneOf(
        choices=['single', 'married']
      )
    )

    risk_questions = fields.List(
      fields.Int(),
      required=True,
      validate=validate.ContainsOnly(
        choices=[0, 1]
      )
    )

    house = fields.Nested(HomeSchema())

    vehicle = fields.Nested(VehicleSchema())

    @validates('age')
    def validate_age(self, value):
        if value < 0 :
            raise EntityError('age must be equals or greater than zero')

    @validates('dependents')
    def validate_dependents(self, value):
        if value < 0 :
            raise EntityError('dependents must be equals or greater than zero')

    @validates('income')
    def validate_income(self, value):
        if value < 0 :
            raise EntityError('income must be equals or greater than zero')

    @validates('risk_questions')
    def validate_risk_questions(self, value):
        if len(value) != 3:
            raise EntityError('risk_questions lenght must be equals three')
