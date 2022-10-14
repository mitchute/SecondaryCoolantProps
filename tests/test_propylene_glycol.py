from unittest import TestCase

from scp.propylene_glycol import PropyleneGlycol


class TestPropyleneGlycol(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = PropyleneGlycol(20.0)

    def test_viscosity(self):
        self.assertAlmostEqual(self.p.viscosity(20), 0.0020300812, delta=1.0e-5)

    def test_specific_heat(self):
        self.assertAlmostEqual(self.p.specific_heat(20), 3976.76, delta=1.0e-2)

    def test_conductivity(self):
        self.assertAlmostEqual(self.p.conductivity(20), 0.4922, delta=1.0e-4)

    def test_density(self):
        self.assertAlmostEqual(self.p.density(20), 1014.77, delta=1.0e-2)
