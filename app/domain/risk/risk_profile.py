from app.domain.risk.risk_score import RiskScore
from app.domain.insurances.auto_insurance import AutoInsurance
from app.domain.insurances.disability_insurance import DisabilityInsurance
from app.domain.insurances.home_insurance import HomeInsurance
from app.domain.insurances.life_insurance import LifeInsurance
import json

class RiskProfile(object):
  def __init__(self):
    self.auto = None
    self.disability = None
    self.home = None
    self.life = None

  def calculate_risk_score(self, data):
    base_score = self._calculate_base_score(data)

    self.auto = RiskScore.execute_calculation(data, AutoInsurance(base_score))
    self.disability = RiskScore.execute_calculation(data, DisabilityInsurance(base_score))
    self.home = RiskScore.execute_calculation(data, HomeInsurance(base_score))
    self.life = RiskScore.execute_calculation(data, LifeInsurance(base_score))

    return self._serialized_response()

  def _calculate_base_score(self, data):
    return sum(data['risk_questions'])

  def _serialized_response(self):
    return json.loads(json.dumps(self.__dict__))
