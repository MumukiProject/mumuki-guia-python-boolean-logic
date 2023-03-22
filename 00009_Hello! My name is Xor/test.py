  
  def test_xor_with_True_and_True_returns_False(self):
    self.assertFalse(xor(True, True))
  
  
  def test_xor_with_True_and_False_returns_True(self):
    self.assertTrue(xor(True, False))
  
  
  def test_xor_with_False_and_True_returns_True(self):
    self.assertTrue(xor(False, True))
  
  
  def test_xor_with_False_and_False_returns_False(self):
    self.assertFalse(xor(False, False))
  
