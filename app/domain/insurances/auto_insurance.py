from app.domain.insurances.insurance import Insurance
from datetime import date


class AutoInsurance(Insurance):
  def _verify_ineligible(self, user_data):
    return 'vehicle' not in user_data

  def _verify_specific_rules(self, user_data):
    self._verify_vehicle(user_data)

  def _verify_vehicle(self, user_data):
    if user_data['vehicle']['year'] >= date.today().year - 5: self.score += 1
