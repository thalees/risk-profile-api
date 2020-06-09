from app.domain.insurances.insurance import Insurance

class DisabilityInsurance(Insurance):
  def _verify_ineligible(self, user_data):
    return user_data['income'] == 0 or user_data['age'] >= 60

  def _verify_specific_rules(self, user_data):
    self._verify_home(user_data)
    self._verify_dependents(user_data)
    self._verify_marital_status(user_data)

  def _verify_home(self, user_data):
    if user_data['house']['ownership_status'] == 'mortgaged': self.score += 1

  def _verify_dependents(self, user_data):
    if user_data['dependents'] > 0: self.score += 1

  def _verify_marital_status(self, user_data):
    if user_data['marital_status'] == 'married' : self.score -= 1
