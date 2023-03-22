  
  def test_es_necesario_que_philosophy_lleve_tilde_y_Greece_esté_en_mayusculas_para_saber_si_la_persona_is_peripatetic(self):
    self.assertTrue(is_peripatetic("philosophy", "Greece", 3))
  
  def test_someone_that_works_in_philosophy_is_from_Greece_and_walks_3k_ms_every_day_is_peripatetic(self):
    self.assertTrue(is_peripatetic("philosophy", "Greece", 3) or is_peripatetic("philosophy", "Greece", 3) or is_peripatetic("philosophy", "Greece", 3) or is_peripatetic("philosophy", "Greece", 3))
  
  def test_someone_that_works_in_philosophy_is_from_Greece_and_walks_2k_ms_every_day_is_not_peripatetic(self):
    self.assertFalse((is_peripatetic("philosophy", "Greece", 2) or is_peripatetic("philosophy", "Greece", 2)))
  
  def test_someone_that_works_in_philosophy_is_from_argentina_and_walks_5k_ms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("philosophy", "Argentina", 5))
  
  def test_someone_that_works_in_atletismo_is_from_Greece_and_walks_10k_ms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("atleta", "Greece", 10))
  
  def test_someone_that_works_in_ingenieria_is_from_colombia_and_walks_1k_ms_every_day_is_not_peripatetic(self):
    self.assertFalse(is_peripatetic("profesor", "Colombia", 1))
  
