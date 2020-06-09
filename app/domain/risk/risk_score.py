class RiskScore(object):

  @staticmethod
  def execute_calculation(data, insurance):
    return insurance.calculate(data)
