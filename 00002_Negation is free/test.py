  
  def test_someone_that_is_20_year_old_is_adult(self):
    self.assertTrue(is_adult(20))
  
  
  def test_someone_that_is_18_year_old_is_adult(self):
    self.assertTrue(is_adult(18))
  
  
  def test_someone_that_is_17_year_old_no_is_adult(self):
    self.assertFalse(is_adult(17))
  
  
  def test_someone_that_is_16_year_old_no_is_adult(self):
    self.assertFalse(is_adult(16))
  
  
  def test_someone_that_is_20_year_old_is_not_minor(self):
    self.assertFalse(is_minor(20))
  
  
  def test_someone_that_is_18_year_old_is_not_minor(self):
    self.assertFalse(is_minor(18))
  
  
  def test_someone_that_is_17_year_old_is_minor(self):
    self.assertTrue(is_minor(17))
  
  
  def test_someone_that_is_16_year_old_is_minor(self):
    self.assertTrue(is_minor(16))
  
