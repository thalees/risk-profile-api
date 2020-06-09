from app.domain.insurances.disability_insurance import DisabilityInsurance


def test_ineligible_classification_by_income():
  base_score = 0
  user_data = _user_data(income= 0)
  insurance = DisabilityInsurance(base_score)

  classification = insurance.calculate(user_data)

  assert classification == 'ineligible'

def test_ineligible_classification_by_age():
  base_score = 0
  user_data = _user_data(age = 70)
  insurance = DisabilityInsurance(base_score)

  classification = insurance.calculate(user_data)

  assert classification == 'ineligible'

def test_increase_score_by_house():
  base_score = 2
  user_data = _user_data(ownership_status= "mortgaged")
  insurance = DisabilityInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def test_increase_score_by_dependents():
  base_score = 2
  user_data = _user_data(dependents = 1)
  insurance = DisabilityInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 3

def test_reduction_score_by_marital_status():
  base_score = 2
  user_data = _user_data(marital_status= "married")
  insurance = DisabilityInsurance(base_score)

  insurance.calculate(user_data)

  assert insurance.score == 1

def _user_data(
    age = 50,
    income=100,
    ownership_status="owned",
    dependents=0,
    marital_status="single"
  ): return {
    "age": age,
    "dependents": dependents,
    "house": {"ownership_status": ownership_status},
    "income": income,
    "marital_status": marital_status,
    "risk_questions": [0, 1, 0],
    "vehicle": {"year": 1999}
  }
