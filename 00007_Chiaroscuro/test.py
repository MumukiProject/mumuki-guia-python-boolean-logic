    
  def test_has_contrast_white_black_is_true(self):
    self.assertTrue(has_contrast("white","black"))

  def test_has_contrast_black_black_is_true(self):
    self.assertTrue(has_contrast("black","black"))

  def test_has_contrast_beige_pink_is_false(self):
    self.assertFalse(has_contrast("beige","pink"))

  def test_has_contrast_pink_blue_is_false(self):
    self.assertFalse(has_contrast("pink","blue"))

  def test_has_contrast_black_yellow_is_true(self):
    self.assertTrue(has_contrast("black","yellow"))