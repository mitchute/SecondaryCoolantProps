from unittest import TestCase

from scp.water import Water


class TestWater(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.p = Water()

    def test_viscosity(self):
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(1.0), 1.731e-03, delta=1.731e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(5.0), 1.518e-03, delta=1.518e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(10.0), 1.306e-03, delta=1.306e-05)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(25.0), 8.900e-04, delta=8.900e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(50.0), 5.465e-04, delta=5.465e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(75.0), 3.774e-04, delta=3.774e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(90.0), 3.142e-04, delta=3.142e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(95.0), 2.971e-04, delta=2.971e-06)

        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'WATER')
        self.assertAlmostEqual(self.p.viscosity(99.0), 2.846e-04, delta=2.846e-06)
