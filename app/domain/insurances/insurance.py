class Insurance(object):
  def __init__(self, base_score):
    self.score = base_score

  def calculate(self, user_data):
    if self._verify_ineligible(user_data):
      return 'ineligible'
    self._verify_general_rules(user_data)
    self._verify_specific_rules(user_data)

    return self.classify()

  def _verify_ineligible(self, user_data): False

  def _verify_general_rules(self, user_data):
    self._verify_age(user_data)
    self._verify_income(user_data)

  def _verify_specific_rules(self, user_data):
    pass

  def classify(self):
    if self.score <= 0:
      return 'economic'
    elif 1 <= self.score <= 2:
      return 'regular'
    else:
      return 'responsible'

  def _verify_age(self, user_data):
    if user_data['age'] < 30: self.score -= 2
    elif 30 <= user_data['age'] <= 40: self.score -= 1

  def _verify_income(self, user_data):
    if user_data['income'] > 200000: self.score -= 1
