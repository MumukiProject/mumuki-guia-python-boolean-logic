def done(): 
  pass

def installments_available(card):
  return {
    'visa': 6,
    'mastercard': 2,
  }.get(card, 1)

def pays_with_credit_card(interest_charged, card, cash_available):
  return not interest_charged and installments_available(card) >= 3 or cash_available < 100
