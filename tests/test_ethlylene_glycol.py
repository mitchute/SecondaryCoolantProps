from unittest import TestCase

from charset_normalizer import detect

from scp.ethylene_glycol import EthyleneGlycol


class TestEthyleneGlycol(TestCase):

    def setUp(self) -> None:
        self.p = EthyleneGlycol(20.0)

    def test_viscosity(self):
        self.assertAlmostEqual(self.p.viscosity(20), 0.0016624202, delta=1.0e-05)

    def test_specific_heat(self):
        self.assertAlmostEqual(self.p.specific_heat(20), 3896.19, delta=1.0e-02)

    def test_conductivity(self):
        self.assertAlmostEqual(self.p.conductivity(20), 0.5076, delta=1.0e-04)

    def test_density(self):
        self.assertAlmostEqual(self.p.density(20), 1024.10, delta=1.0e-02)

    def test_freeze_point(self):
        self.assertAlmostEqual(self.p.calc_freeze_point(20), -7.796, delta=1.0e-03)