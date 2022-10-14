from unittest import TestCase

from scp.ethyl_alcohol import EthylAlcohol


class TestPropyleneGlycol(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = EthylAlcohol(20.0)

    def test_viscosity(self):
        self.assertAlmostEqual(self.p.viscosity(20), 0.00216475, delta=1.0e-5)

    def test_specific_heat(self):
        self.assertAlmostEqual(self.p.specific_heat(20), 4328.65, delta=1.0e-2)

    def test_conductivity(self):
        self.assertAlmostEqual(self.p.conductivity(20), 0.4663, delta=1.0e-4)

    def test_density(self):
        self.assertAlmostEqual(self.p.density(20), 968.91, delta=1.0e-2)
