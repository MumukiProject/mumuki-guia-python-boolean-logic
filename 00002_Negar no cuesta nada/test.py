def test_alguien_de_20_anios_es_mayor_de_edad(self):
  self.assertEqual(es_mayor_de_edad(20), True)


def test_alguien_de_18_anios_es_mayor_de_edad(self):
  self.assertEqual(es_mayor_de_edad(18), True)


def test_alguien_de_17_anios_no_es_mayor_de_edad(self):
  self.assertEqual(es_mayor_de_edad(17), False)


def test_alguien_de_16_anios_no_es_mayor_de_edad(self):
  self.assertEqual(es_mayor_de_edad(16), False)


def test_alguien_de_20_anios_no_es_menor_de_edad(self):
  self.assertEqual(es_menor_de_edad(20), False)


def test_alguien_de_18_anios_no_es_menor_de_edad(self):
  self.assertEqual(es_menor_de_edad(18), False)


def test_alguien_de_17_anios_es_menor_de_edad(self):
  self.assertEqual(es_menor_de_edad(17), True)


def test_alguien_de_16_anios_es_menor_de_edad(self):
  self.assertEqual(es_menor_de_edad(16), True)
