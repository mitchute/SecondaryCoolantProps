from unittest import TestCase

from scp.ethylene_glycol import EthyleneGlycol


class TestEthyleneGlycolConcentration0(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = EthyleneGlycol(0.0)

    def test_viscosity_conc(self):
        # T: 1 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(1.0), 1.721e-03, delta=3.441e-05)

        # T: 5 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(5.0), 1.519e-03, delta=3.037e-05)

        # T: 10 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(10.0), 1.312e-03, delta=2.623e-05)

        # T: 25 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(25.0), 8.953e-04, delta=1.791e-05)

        # T: 50 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(50.0), 5.520e-04, delta=1.104e-05)

        # T: 75 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 75, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(75.0), 3.835e-04, delta=7.670e-06)

        # T: 90 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 90, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(90.0), 3.155e-04, delta=6.309e-06)

        # T: 95 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 95, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(95.0), 2.955e-04, delta=5.911e-06)

        # T: 99 [C], Conc: 0.0 [-], ErrTol: 2.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 99, 'INCOMP::MEG[0.0000]')
        self.assertAlmostEqual(self.p.viscosity(99.0), 2.803e-04, delta=5.606e-06)

class TestEthyleneGlycolConcentration20(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.p = EthyleneGlycol(0.2)

    def test_viscosity(self):
        # T: 1 [C], Conc: 0.2 [-], ErrTol: 15.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 1, 'INCOMP::MEG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(1.0), 3.064e-03, delta=4.595e-04)

        # T: 5 [C], Conc: 0.2 [-], ErrTol: 15.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 5, 'INCOMP::MEG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(5.0), 2.659e-03, delta=3.989e-04)

        # T: 10 [C], Conc: 0.2 [-], ErrTol: 15.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 10, 'INCOMP::MEG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(10.0), 2.250e-03, delta=3.376e-04)

        # T: 25 [C], Conc: 0.2 [-], ErrTol: 15.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 25, 'INCOMP::MEG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(25.0), 1.450e-03, delta=2.175e-04)

        # T: 50 [C], Conc: 0.2 [-], ErrTol: 15.0%
        # PropsSI('V', 'P', 101325, 'T', 273.15 + 50, 'INCOMP::MEG[0.2000]')
        self.assertAlmostEqual(self.p.viscosity(50.0), 8.294e-04, delta=1.244e-04)
