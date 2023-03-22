  
  def test_monday_holiday_at_14_the_bank_is_not_open(self):
    self.assertFalse(is_bank_open(True, "Monday", 14))
  
  def test_wednesday_holiday_at_20_the_bank_is_not_open(self):
    self.assertFalse(is_bank_open(True, "Wednesday", 20))
  
  def test_thursday_at_13_the_bank_is_open(self):
    self.assertTrue(is_bank_open(False, "Thursday", 13))
  
  def test_saturday_at_11_the_bank_is_not_open(self):
    self.assertFalse(is_bank_open(False, "Saturday", 11))
  
  def test_monday_at_19_the_bank_is_not_open(self):
    self.assertFalse(is_bank_open(False, "Monday", 19))
    
  def test_tuesday_at_16_the_bank_is_not_open(self):
    self.assertFalse(is_bank_open(False, "Tuesday", 16))
  
