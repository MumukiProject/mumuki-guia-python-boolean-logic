  
  def test_can_focus_te_95_True_is_True(self):
    self.assertTrue(can_focus("tea",95, True))

  def test_can_focus_tea_100_True_is_True(self):
    self.assertTrue(can_focus("tea",100, True))

  def test_can_focus_mate_80_True_is_True(self):
    self.assertTrue(can_focus('mate', 80, True))

  def test_can_focus_mate_70_True_is_False(self):
    self.assertFalse(can_focus('mate', 70, True))

  def test_can_focus_tea_94_True_is_False(self):
    self.assertFalse(can_focus("tea",94, True))

  def test_can_focus_tea_95_False_is_False(self):
    self.assertFalse(can_focus("tea",95, False))
    
