from unittest import TestCase

from scp.propylene_glycol import PropyleneGlycol


class TestPropyleneGlycol(TestCase):
    def test_1(self):

        p = PropyleneGlycol(0.0)

        # Visc @ T=5degC, X=0: 1.5364e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 1.5364e-03, delta=1.5364e-06)

        # Dens @ T=5degC, X=0: 1.0003e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0003e03, delta=1.0003e00)

        # SpHt @ T=5degC, X=0: 4.2048e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.2048e03, delta=4.2048e00)

        # Cond @ T=5degC, X=0: 5.7124e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 5.7124e-01, delta=5.7124e-04)

        # Visc @ T=20degC, X=0: 1.0072e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.0072e-03, delta=1.0072e-06)

        # Dens @ T=20degC, X=0: 9.9852e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.9852e02, delta=9.9852e-01)

        # SpHt @ T=20degC, X=0: 4.1866e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1866e03, delta=4.1866e00)

        # Cond @ T=20degC, X=0: 5.9913e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.9913e-01, delta=5.9913e-04)

        # Visc @ T=40degC, X=0: 6.5033e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 6.5033e-04, delta=6.5033e-07)

        # Dens @ T=40degC, X=0: 9.9253e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.9253e02, delta=9.9253e-01)

        # SpHt @ T=40degC, X=0: 4.1783e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.1783e03, delta=4.1783e00)

        # Cond @ T=40degC, X=0: 6.3007e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 6.3007e-01, delta=6.3007e-04)

    def test_2(self):

        p = PropyleneGlycol(0.2)

        # Visc @ T=5degC, X=0.2: 3.4941e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 3.4941e-03, delta=3.4941e-06)

        # Dens @ T=5degC, X=0.2: 1.0191e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0191e03, delta=1.0191e00)

        # SpHt @ T=5degC, X=0.2: 3.9459e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.9459e03, delta=3.9459e00)

        # Cond @ T=5degC, X=0.2: 4.7647e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.7647e-01, delta=4.7647e-04)

        # Visc @ T=20degC, X=0.2: 2.0301e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 2.0301e-03, delta=2.0301e-06)

        # Dens @ T=20degC, X=0.2: 1.0148e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0148e03, delta=1.0148e00)

        # SpHt @ T=20degC, X=0.2: 3.9768e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.9768e03, delta=3.9768e00)

        # Cond @ T=20degC, X=0.2: 4.9221e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.9221e-01, delta=4.9221e-04)

        # Visc @ T=40degC, X=0.2: 1.1693e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.1693e-03, delta=1.1693e-06)

        # Dens @ T=40degC, X=0.2: 1.0064e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0064e03, delta=1.0064e00)

        # SpHt @ T=40degC, X=0.2: 4.0190e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.0190e03, delta=4.0190e00)

        # Cond @ T=40degC, X=0.2: 5.1228e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 5.1228e-01, delta=5.1228e-04)

    def test_3(self):

        p = PropyleneGlycol(0.4)

        # Visc @ T=5degC, X=0.4: 8.9817e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 8.9817e-03, delta=8.9817e-06)

        # Dens @ T=5degC, X=0.4: 1.0401e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0401e03, delta=1.0401e00)

        # SpHt @ T=5degC, X=0.4: 3.6580e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.6580e03, delta=3.6580e00)

        # Cond @ T=5degC, X=0.4: 3.9089e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 3.9089e-01, delta=3.9089e-04)

        # Visc @ T=20degC, X=0.4: 4.3838e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 4.3838e-03, delta=4.3838e-06)

        # Dens @ T=20degC, X=0.4: 1.0323e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0323e03, delta=1.0323e00)

        # SpHt @ T=20degC, X=0.4: 3.7067e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.7067e03, delta=3.7067e00)

        # Cond @ T=20degC, X=0.4: 4.0026e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.0026e-01, delta=4.0026e-04)

        # Visc @ T=40degC, X=0.4: 2.1408e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 2.1408e-03, delta=2.1408e-06)

        # Dens @ T=40degC, X=0.4: 1.0201e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0201e03, delta=1.0201e00)

        # SpHt @ T=40degC, X=0.4: 3.7708e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.7708e03, delta=3.7708e00)

        # Cond @ T=40degC, X=0.4: 4.1321e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 4.1321e-01, delta=4.1321e-04)

    def test_t_freeze(self):
        # T_freeze @ X=0.1: -2.867. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.1).freeze_point(0.1), -2.867, delta=1.0e-02)

        # T_freeze @ X=0.2: -7.173. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.2).freeze_point(0.2), -7.173, delta=1.0e-02)

        # T_freeze @ X=0.3: -12.789. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.3).freeze_point(0.3), -12.789, delta=1.0e-02)

        # T_freeze @ X=0.4: -20.568. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.4).freeze_point(0.4), -20.568, delta=1.0e-02)

        # T_freeze @ X=0.5: -32.193. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.5).freeze_point(0.5), -32.193, delta=1.0e-02)

        # T_freeze @ X=0.6: -50.003. ErrTol=0.01C
        self.assertAlmostEqual(PropyleneGlycol(0.6).freeze_point(0.6), -50.003, delta=1.0e-02)
