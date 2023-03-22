  
  def test_tiene_contraste_blanco_negro_es_verdadero(self):
    self.assertTrue(tiene_contraste("blanco","negro"))

  def test_tiene_contraste_beige_rosa_es_falso(self):
    self.assertFalse(tiene_contraste("beige","rosa"))

  def test_tiene_contraste_rojo_azul_es_falso(self):
    self.assertFalse(tiene_contraste("rojo","azul"))

  def test_tiene_contraste_negro_amarillo_es_verdadero(self):
    self.assertTrue(tiene_contraste("negro","amarillo"))