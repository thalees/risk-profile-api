from app.domain.insurances.home_insurance import HomeInsurance


def test_ineligible_classification():
  base_score = 0
  user_data = _user_data_without_house()
  insurance = HomeInsurance(base_score)

  classification = insurance.calculate(user_data)

  assert classification == 'ineligible'

def test_increase_score_by_house():
  base_score = 2
  user_data = _user_data(age= 50, income= 100, ownership_status= "mortgaged")
  insurance = HomeInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def _user_data(age, income, ownership_status):
  return {
    "age": age,
    "dependents": 2,
    "house": {"ownership_status": ownership_status},
    "income": income,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 1999}
  }

def _user_data_without_house():
  return {
    "age": 35,
    "dependents": 2,
    "income": 0,
    "marital_status": "married",
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 1999}
  }
