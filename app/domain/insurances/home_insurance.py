from app.domain.insurances.insurance import Insurance

class HomeInsurance(Insurance):
  def _verify_ineligible(self, user_data):
    return 'house' not in user_data

  def _verify_specific_rules(self, user_data):
    self._verify_home(user_data)

  def _verify_home(self, user_data):
    if user_data['house']['ownership_status'] == 'mortgaged': self.score += 1
