import json

from flask import Flask, jsonify, request
from app.domain.risk.risk_profile import RiskProfile
from app.infra.validator import validate_schema
from app.api.validator.user_post_shema import UserPostSchema

server = Flask(__name__)

@server.route("/risk-profile", methods=["POST"])
@validate_schema(UserPostSchema())
def api():
  user_data = request.json
  risk_profile = RiskProfile()

  return risk_profile.calculate_risk_score(user_data), 201

if __name__ == "__main__":
  server.run()
