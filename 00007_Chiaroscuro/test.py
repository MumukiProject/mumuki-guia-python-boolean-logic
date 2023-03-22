  
  def test_has_contrast_white_black_is_True(self):
    self.assertTrue(has_contrast("white","black"))

  def test_has_contrast_beige_pink_is_False(self):
    self.assertFalse(has_contrast("beige","pink"))

  def test_has_contrast_red_blue_is_False(self):
    self.assertFalse(has_contrast("red","blue"))

  def test_has_contrast_black_yellow_is_True(self):
    self.assertTrue(has_contrast("black","yellow"))