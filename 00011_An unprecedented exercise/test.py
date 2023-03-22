  
  def test_se_puede_concentrar_te_95_true_es_verdadero(self):
    self.assertTrue(se_puede_concentrar("té",95, True))

  def test_se_puede_concentrar_té_100_true_es_verdadero(self):
    self.assertTrue(se_puede_concentrar("té",100, True))

  def test_se_puede_concentrar_mate_80_true_es_verdadero(self):
    self.assertTrue(se_puede_concentrar('mate', 80, True))

  def test_se_puede_concentrar_mate_70_true_es_falso(self):
    self.assertFalse(se_puede_concentrar('mate', 70, True))

  def test_se_puede_concentrar_t_94_true_es_falso(self):
    self.assertFalse(se_puede_concentrar("té",94, True))

  def test_se_puede_concentrar_té_95_false_es_falso(self):
    self.assertFalse(se_puede_concentrar("té",95, False))