from app.domain.insurances.insurance import Insurance


def test_reduction_score_by_age_under_30():
  base_score = 2
  user_data = _user_data(age= 29, income= 100, vehicle_year= 1999)
  auto_insurance = Insurance(base_score)

  auto_insurance.calculate(user_data)

  assert auto_insurance.score == 0

def test_reduction_score_by_age_between_30_and_40():
  base_score = 2
  user_data = _user_data(age= 35, income= 100, vehicle_year= 1999)
  auto_insurance = Insurance(base_score)

  auto_insurance.calculate(user_data)

  assert auto_insurance.score == 1

def test_reduction_score_by_income():
  base_score = 2
  user_data = _user_data(age= 50, income= 300000, vehicle_year= 1999)
  auto_insurance = Insurance(base_score)

  auto_insurance.calculate(user_data)

  assert auto_insurance.score == 1

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
