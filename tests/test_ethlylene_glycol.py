from unittest import TestCase

from scp.ethylene_glycol import EthyleneGlycol


class TestEthyleneGlycol(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = EthyleneGlycol(0.0)

    def test_viscosity(self):
        self.assertAlmostEqual(self.p.viscosity(1.0), 0.0016624202, delta=1.0e-05)

    def test_specific_heat(self):
        self.assertAlmostEqual(self.p.specific_heat(20), 3896.19, delta=1.0e-2)

    def test_conductivity(self):
        self.assertAlmostEqual(self.p.conductivity(20), 0.5076, delta=1.0e-4)

    def test_density(self):
        self.assertAlmostEqual(self.p.density(20), 1024.10, delta=1.0e-2)
