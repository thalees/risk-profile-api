from app.domain.insurances.auto_insurance import AutoInsurance

def test_ineligible_classification():
  base_score = 0
  user_data = _user_data_without_vehicle()
  insurance = AutoInsurance(base_score)

  classification = insurance.calculate(user_data)

  assert classification == 'ineligible'

def test_increase_score_by_vehicle():
  base_score = 2
  user_data = _user_data(age= 50, income= 100, vehicle_year= 2018)
  insurance = AutoInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def _user_data(age, income, vehicle_year):
  return {
    "age": age,
    "dependents": 2,
    "house": {"ownership_status": "owned"},
    "income": income,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": vehicle_year}
  }

def _user_data_without_vehicle():
  return {
    "age": 35,
    "dependents": 2,
    "house": {"ownership_status": "owned"},
    "income": 0,
    "marital_status": "married",
    "risk_questions": [0, 1, 0]
  }
