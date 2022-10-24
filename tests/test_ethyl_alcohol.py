from unittest import TestCase

from scp.ethyl_alcohol import EthylAlcohol


class TestPropyleneGlycol(TestCase):
    def test_1(self):

        p = EthylAlcohol(0.0)

        # Visc @ T=5degC, X=0: 1.5015e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 1.5015e-03, delta=1.5015e-06)

        # Dens @ T=5degC, X=0: 1.0001e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0001e03, delta=1.0001e00)

        # SpHt @ T=5degC, X=0: 4.2052e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.2052e03, delta=4.2052e00)

        # Cond @ T=5degC, X=0: 5.7090e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 5.7090e-01, delta=5.7090e-04)

        # Visc @ T=20degC, X=0: 1.0005e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.0005e-03, delta=1.0005e-06)

        # Dens @ T=20degC, X=0: 9.9818e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.9818e02, delta=9.9818e-01)

        # SpHt @ T=20degC, X=0: 4.1683e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1683e03, delta=4.1683e00)

        # Cond @ T=20degC, X=0: 5.9802e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.9802e-01, delta=5.9802e-04)

        # Visc @ T=40degC, X=0: 6.5457e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 6.5457e-04, delta=6.5457e-07)

        # Dens @ T=40degC, X=0: 9.9244e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.9244e02, delta=9.9244e-01)

        # SpHt @ T=40degC, X=0: 4.2005e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.2005e03, delta=4.2005e00)

        # Cond @ T=40degC, X=0: 6.3014e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 6.3014e-01, delta=6.3014e-04)

    def test_2(self):

        p = EthylAlcohol(0.2)

        # Visc @ T=5degC, X=0.2: 4.0621e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 4.0621e-03, delta=4.0621e-06)

        # Dens @ T=5degC, X=0.2: 9.7442e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.7442e02, delta=9.7442e-01)

        # SpHt @ T=5degC, X=0.2: 4.3595e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.3595e03, delta=4.3595e00)

        # Cond @ T=5degC, X=0.2: 4.5243e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.5243e-01, delta=4.5243e-04)

        # Visc @ T=20degC, X=0.2: 2.1648e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 2.1648e-03, delta=2.1648e-06)

        # Dens @ T=20degC, X=0.2: 9.6892e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.6892e02, delta=9.6892e-01)

        # SpHt @ T=20degC, X=0.2: 4.3287e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.3287e03, delta=4.3287e00)

        # Cond @ T=20degC, X=0.2: 4.6631e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.6631e-01, delta=4.6631e-04)

        # Visc @ T=40degC, X=0.2: 1.1640e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.1640e-03, delta=1.1640e-06)

        # Dens @ T=40degC, X=0.2: 9.5881e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.5881e02, delta=9.5881e-01)

        # SpHt @ T=40degC, X=0.2: 4.3200e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.3200e03, delta=4.3200e00)

        # Cond @ T=40degC, X=0.2: 4.8440e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 4.8440e-01, delta=4.8440e-04)

    def test_3(self):

        p = EthylAlcohol(0.4)

        # Visc @ T=5degC, X=0.4: 5.5016e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 5.5016e-03, delta=5.5016e-06)

        # Dens @ T=5degC, X=0.4: 9.4601e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.4601e02, delta=9.4601e-01)

        # SpHt @ T=5degC, X=0.4: 3.9315e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.9315e03, delta=3.9315e00)

        # Cond @ T=5degC, X=0.4: 3.5458e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 3.5458e-01, delta=3.5458e-04)

        # Visc @ T=20degC, X=0.4: 2.8758e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 2.8758e-03, delta=2.8758e-06)

        # Dens @ T=20degC, X=0.4: 9.3532e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.3532e02, delta=9.3532e-01)

        # SpHt @ T=20degC, X=0.4: 4.0293e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.0293e03, delta=4.0293e00)

        # Cond @ T=20degC, X=0.4: 3.6120e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 3.6120e-01, delta=3.6120e-04)

        # Visc @ T=40degC, X=0.4: 1.4573e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.4573e-03, delta=1.4573e-06)

        # Dens @ T=40degC, X=0.4: 9.2026e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.2026e02, delta=9.2026e-01)

        # SpHt @ T=40degC, X=0.4: 4.1199e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.1199e03, delta=4.1199e00)

        # Cond @ T=40degC, X=0.4: 3.6934e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 3.6934e-01, delta=3.6934e-04)

    def test_t_freeze(self):
        # T_freeze @ X=0.1: -4.379. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.1).freeze_point(0.1), -4.379, delta=1.0e-02)

        # T_freeze @ X=0.2: -11.119. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.2).freeze_point(0.2), -11.119, delta=1.0e-02)

        # T_freeze @ X=0.3: -20.140. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.3).freeze_point(0.3), -20.140, delta=1.0e-02)

        # T_freeze @ X=0.4: -29.533. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.4).freeze_point(0.4), -29.533, delta=1.0e-02)

        # T_freeze @ X=0.5: -37.611. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.5).freeze_point(0.5), -37.611, delta=1.0e-02)

        # T_freeze @ X=0.6: -44.910. ErrTol=0.01C
        self.assertAlmostEqual(EthylAlcohol(0.6).freeze_point(0.6), -44.910, delta=1.0e-02)
