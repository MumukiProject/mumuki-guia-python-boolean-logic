  
  def test_greece_must_be_written_with_uppercase_g_in_order_to_be_peripatetic(self):
    self.assertTrue(is_peripatetic("philosophy", "Greece", 3))
  
  def test_someone_that_works_in_philosophy_is_from_Greece_and_walks_3_kms_every_day_is_peripatetic(self):
    self.assertTrue(is_peripatetic("philosophy", "Greece", 3) or is_peripatetic("philosophy", "greece", 3))
  
  def test_someone_that_works_in_philosophy_is_from_Greece_and_walks_2_kms_every_day_is_not_peripatetic(self):
    self.assertFalse((is_peripatetic("philosophy", "Greece", 2) or is_peripatetic("philosophy", "greece", 2)))
  
  def test_someone_that_works_in_philosophy_is_from_argentina_and_walks_5_kms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("philosophy", "Argentina", 5))
  
  def test_someone_that_works_in_atletismo_is_from_Greece_and_walks_10_kms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("atleta", "Greece", 10))
  
  def test_someone_that_works_in_ingenieria_is_from_colombia_and_walks_1_kms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("profesor", "Colombia", 1))
  
