from unittest import TestCase

from scp.methyl_alcohol import MethylAlcohol


class TestMethylAlcohol(TestCase):
    def test_1(self):

        p = MethylAlcohol(0.0)

        # Visc @ T=5degC, X=0: 1.5169e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 1.5169e-03, delta=1.5169e-06)

        # Dens @ T=5degC, X=0: 1.0000e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0000e03, delta=1.0000e00)

        # SpHt @ T=5degC, X=0: 4.2159e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.2159e03, delta=4.2159e00)

        # Cond @ T=5degC, X=0: 5.7057e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 5.7057e-01, delta=5.7057e-04)

        # Visc @ T=20degC, X=0: 1.0000e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.0000e-03, delta=1.0000e-06)

        # Dens @ T=20degC, X=0: 9.9841e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.9841e02, delta=9.9841e-01)

        # SpHt @ T=20degC, X=0: 4.1649e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1649e03, delta=4.1649e00)

        # Cond @ T=20degC, X=0: 5.9834e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.9834e-01, delta=5.9834e-04)

        # Visc @ T=40degC, X=0: 6.5422e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 6.5422e-04, delta=6.5422e-07)

        # Dens @ T=40degC, X=0: 9.9216e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.9216e02, delta=9.9216e-01)

        # SpHt @ T=40degC, X=0: 4.1802e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.1802e03, delta=4.1802e00)

        # Cond @ T=40degC, X=0: 6.2986e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 6.2986e-01, delta=6.2986e-04)

    def test_2(self):

        p = MethylAlcohol(0.2)

        # Visc @ T=5degC, X=0.2: 2.6531e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 2.6531e-03, delta=2.6531e-06)

        # Dens @ T=5degC, X=0.2: 9.7135e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.7135e02, delta=9.7135e-01)

        # SpHt @ T=5degC, X=0.2: 4.0832e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.0832e03, delta=4.0832e00)

        # Cond @ T=5degC, X=0.2: 4.6748e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.6748e-01, delta=4.6748e-04)

        # Visc @ T=20degC, X=0.2: 1.5979e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.5979e-03, delta=1.5979e-06)

        # Dens @ T=20degC, X=0.2: 9.6679e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.6679e02, delta=9.6679e-01)

        # SpHt @ T=20degC, X=0.2: 4.1101e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1101e03, delta=4.1101e00)

        # Cond @ T=20degC, X=0.2: 4.8339e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.8339e-01, delta=4.8339e-04)

        # Visc @ T=40degC, X=0.2: 9.4179e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 9.4179e-04, delta=9.4179e-07)

        # Dens @ T=40degC, X=0.2: 9.5837e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.5837e02, delta=9.5837e-01)

        # SpHt @ T=40degC, X=0.2: 4.0980e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.0980e03, delta=4.0980e00)

        # Cond @ T=40degC, X=0.2: 5.0402e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 5.0402e-01, delta=5.0402e-04)

    def test_3(self):

        p = MethylAlcohol(0.4)

        # Visc @ T=5degC, X=0.4: 3.0165e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 3.0165e-03, delta=3.0165e-06)

        # Dens @ T=5degC, X=0.4: 9.4305e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.4305e02, delta=9.4305e-01)

        # SpHt @ T=5degC, X=0.4: 3.7171e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.7171e03, delta=3.7171e00)

        # Cond @ T=5degC, X=0.4: 3.7833e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 3.7833e-01, delta=3.7833e-04)

        # Visc @ T=20degC, X=0.4: 1.8385e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.8385e-03, delta=1.8385e-06)

        # Dens @ T=20degC, X=0.4: 9.3457e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.3457e02, delta=9.3457e-01)

        # SpHt @ T=20degC, X=0.4: 3.8224e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.8224e03, delta=3.8224e00)

        # Cond @ T=20degC, X=0.4: 3.8571e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 3.8571e-01, delta=3.8571e-04)

        # Visc @ T=40degC, X=0.4: 1.0684e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.0684e-03, delta=1.0684e-06)

        # Dens @ T=40degC, X=0.4: 9.2227e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.2227e02, delta=9.2227e-01)

        # SpHt @ T=40degC, X=0.4: 3.8728e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.8728e03, delta=3.8728e00)

        # Cond @ T=40degC, X=0.4: 3.9646e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 3.9646e-01, delta=3.9646e-04)

    def test_t_freeze(self):
        # T_freeze @ X=0.1: -6.540. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.1).freeze_point(0.1), -6.540, delta=1.0e-02)

        # T_freeze @ X=0.2: -15.080. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.2).freeze_point(0.2), -15.080, delta=1.0e-02)

        # T_freeze @ X=0.3: -25.685. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.3).freeze_point(0.3), -25.685, delta=1.0e-02)

        # T_freeze @ X=0.4: -38.703. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.4).freeze_point(0.4), -38.703, delta=1.0e-02)

        # T_freeze @ X=0.5: -54.466. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.5).freeze_point(0.5), -54.466, delta=1.0e-02)

        # T_freeze @ X=0.6: -73.006. ErrTol=0.01C
        self.assertAlmostEqual(MethylAlcohol(0.6).freeze_point(0.6), -73.006, delta=1.0e-02)
