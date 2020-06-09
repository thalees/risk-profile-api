from app.domain.insurances.life_insurance import LifeInsurance


def test_ineligible_classification_by_age():
  base_score = 0
  user_data = _user_data(age = 70)
  insurance = LifeInsurance(base_score)

  classification = insurance.calculate(user_data)

  assert classification == 'ineligible'

def test_increase_score_by_dependents():
  base_score = 2
  user_data = _user_data(dependents = 1)
  insurance = LifeInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def test_increase_score_by_marital_status():
  base_score = 2
  user_data = _user_data(marital_status= "married")
  insurance = LifeInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def _user_data(age=50, dependents=0, marital_status="single"):
  return {
    "age": age,
    "dependents": dependents,
    "house": {"ownership_status": "owned"},
    "income": 100,
    "marital_status": marital_status,
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 2018}
  }
