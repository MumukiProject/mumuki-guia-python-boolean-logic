
  def test_someone_who_is_1__DT__5_m_and_is_not_accompanied_by_an_adult_and_has_no_hearth_conditions_can_ride(self):
    self.assertTrue(can_ride(1.5, False, False))

  def test_someone_who_is_1__DT__7_m_and_is_not_accompanied_by_an_adult_and_has_a_hearth_condition_cannot_ride(self):
    self.assertFalse(can_ride(1.7, False, True))

  def test_someone_who_is_1__DT__3_m_and_is_accompanied_by_an_adult_and_has_a_hearth_condition_cannot_ride(self):
    self.assertFalse(can_ride(1.3, True, True))  

  def test_someone_who_is_1__DT__2_m_and_is_accompanied_by_an_adult_and_has_no_hearth_conditions_can_ride(self):
    self.assertTrue(can_ride(1.2, True, False))

  def test_someone_who_is_1__DT__2_m_and_is_not_accompanied_by_an_adult_and_has_no_hearth_conditions_cannot_ride(self):
    self.assertFalse(can_ride(1.2, False, False))

  def test_someone_who_is_1__DT__1_m_and_is_accompanied_by_an_adult_and_has_no_hearth_conditions_cannot_ride(self):
    self.assertFalse(can_ride(1.1, True, False))

