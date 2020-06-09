from app.domain.risk.risk_score import RiskScore
from app.domain.insurances.insurance import Insurance


def test_risk_score_mapped_to_economic_range():
  first_insurance = Insurance(base_score=0)
  second_insurance = Insurance(base_score=0)
  user_data = _user_data()

  first_insurance.score = 0
  second_insurance.score = -3

  first_range = RiskScore.execute_calculation(user_data, first_insurance)
  second_range = RiskScore.execute_calculation(user_data, second_insurance)

  assert first_range == "economic"
  assert second_range == "economic"

def test_risk_score_mapped_to_regular_range():
  first_insurance = Insurance(base_score=0)
  second_insurance = Insurance(base_score=0)
  user_data = _user_data()

  first_insurance.score = 1
  second_insurance.score = 2

  first_range = RiskScore.execute_calculation(user_data, first_insurance)
  second_range = RiskScore.execute_calculation(user_data, second_insurance)

  assert first_range == "regular"
  assert second_range == "regular"

def test_risk_score_mapped_to_responsible_range():
  first_insurance = Insurance(base_score=0)
  second_insurance = Insurance(base_score=0)
  user_data = _user_data()

  first_insurance.score = 3
  second_insurance.score = 6

  first_range = RiskScore.execute_calculation(user_data, first_insurance)
  second_range = RiskScore.execute_calculation(user_data, second_insurance)

  assert first_range == "responsible"
  assert second_range == "responsible"

def _user_data():
  return {
    "age": 50,
    "dependents": 2,
    "house": {"ownership_status": "owned"},
    "income": 1000,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 2018}
  }
