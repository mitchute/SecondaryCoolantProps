from unittest import TestCase

from scp.propylene_glycol import PropyleneGlycol


class TestPropyleneGlycolConcentration0(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = PropyleneGlycol(0.0)

    def test_viscosity_conc_0(self):
        # T: 1 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(1.0), 1.748e-03, delta=3.495e-05)

        # T: 5 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(5.0), 1.536e-03, delta=3.073e-05)

        # T: 10 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(10.0), 1.321e-03, delta=2.642e-05)

        # T: 25 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(25.0), 8.920e-04, delta=1.784e-05)

        # T: 50 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(50.0), 5.450e-04, delta=1.090e-05)

        # T: 75 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(75.0), 3.799e-04, delta=7.597e-06)

        # T: 90 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(90.0), 3.150e-04, delta=6.300e-06)

        # T: 95 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(95.0), 2.962e-04, delta=5.924e-06)

        # T: 99 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'INCOMP::MPG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(99.0), 2.819e-04, delta=5.637e-06)


class TestPropyleneGlycolConcentration20(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = PropyleneGlycol(0.2)

    def test_viscosity(self):
        # T: 1 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(1.0), 4.129e-03, delta=3.304e-04)

        # T: 5 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(5.0), 3.494e-03, delta=2.795e-04)

        # T: 10 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(10.0), 2.875e-03, delta=2.300e-04)

        # T: 25 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(25.0), 1.739e-03, delta=1.391e-04)

        # T: 50 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(50.0), 9.400e-04, delta=7.520e-05)

        # T: 75 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(75.0), 6.080e-04, delta=4.864e-05)

        # T: 90 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(90.0), 4.869e-04, delta=3.895e-05)

        # T: 95 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(95.0), 4.527e-04, delta=3.621e-05)

        # T: 99 [C], Conc: 0.2 [-], ErrTol: 8.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'INCOMP::MPG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(99.0), 4.268e-04, delta=3.414e-05)


class TestPropyleneGlycolConcentration40(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = PropyleneGlycol(0.4)

    def test_viscosity(self):
        # T: 1 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(1.0), 1.121e-02, delta=1.121e-03)

        # T: 5 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(5.0), 8.982e-03, delta=8.982e-04)

        # T: 10 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(10.0), 6.935e-03, delta=6.935e-04)

        # T: 25 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(25.0), 3.580e-03, delta=3.580e-04)

        # T: 50 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(50.0), 1.623e-03, delta=1.623e-04)

        # T: 75 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(75.0), 9.546e-04, delta=9.546e-05)

        # T: 90 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(90.0), 7.398e-04, delta=7.398e-05)

        # T: 95 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(95.0), 6.819e-04, delta=6.819e-05)

        # T: 99 [C], Conc: 0.4 [-], ErrTol: 10.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'INCOMP::MPG[0.4000]')
        self.assertAlmostEqual(self.p.viscosity(99.0), 6.389e-04, delta=6.389e-05)
