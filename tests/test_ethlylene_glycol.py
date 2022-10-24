from unittest import TestCase

from scp.ethylene_glycol import EthyleneGlycol


class TestEthyleneGlycol(TestCase):
    def test_1(self):

        p = EthyleneGlycol(0.0)

        # Visc @ T=5degC, X=0: 1.5186e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 1.5186e-03, delta=1.5186e-06)

        # Dens @ T=5degC, X=0: 9.9915e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.9915e02, delta=9.9915e-01)

        # SpHt @ T=5degC, X=0: 4.2027e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.2027e03, delta=4.2027e00)

        # Cond @ T=5degC, X=0: 5.7137e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 5.7137e-01, delta=5.7137e-04)

        # Visc @ T=20degC, X=0: 1.0078e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.0078e-03, delta=1.0078e-06)

        # Dens @ T=20degC, X=0: 9.9735e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.9735e02, delta=9.9735e-01)

        # SpHt @ T=20degC, X=0: 4.1862e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1862e03, delta=4.1862e00)

        # Cond @ T=20degC, X=0: 5.9913e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.9913e-01, delta=5.9913e-04)

        # Visc @ T=40degC, X=0: 6.5721e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 6.5721e-04, delta=6.5721e-07)

        # Dens @ T=40degC, X=0: 9.9181e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.9181e02, delta=9.9181e-01)

        # SpHt @ T=40degC, X=0: 4.1785e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.1785e03, delta=4.1785e00)

        # Cond @ T=40degC, X=0: 6.2983e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 6.2983e-01, delta=6.2983e-04)

    def test_2(self):

        p = EthyleneGlycol(0.2)

        # Visc @ T=5degC, X=0.2: 2.6594e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 2.6594e-03, delta=2.6594e-06)

        # Dens @ T=5degC, X=0.2: 1.0281e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0281e03, delta=1.0281e00)

        # SpHt @ T=5degC, X=0.2: 3.8695e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.8695e03, delta=3.8695e00)

        # Cond @ T=5degC, X=0.2: 4.9022e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.9022e-01, delta=4.9022e-04)

        # Visc @ T=20degC, X=0.2: 1.6624e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.6624e-03, delta=1.6624e-06)

        # Dens @ T=20degC, X=0.2: 1.0241e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0241e03, delta=1.0241e00)

        # SpHt @ T=20degC, X=0.2: 3.8962e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.8962e03, delta=3.8962e00)

        # Cond @ T=20degC, X=0.2: 5.0766e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.0766e-01, delta=5.0766e-04)

        # Visc @ T=40degC, X=0.2: 1.0133e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.0133e-03, delta=1.0133e-06)

        # Dens @ T=40degC, X=0.2: 1.0164e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0164e03, delta=1.0164e00)

        # SpHt @ T=40degC, X=0.2: 3.9328e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.9328e03, delta=3.9328e00)

        # Cond @ T=40degC, X=0.2: 5.2908e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 5.2908e-01, delta=5.2908e-04)

    def test_3(self):

        p = EthyleneGlycol(0.4)

        # Visc @ T=5degC, X=0.4: 4.7569e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 4.7569e-03, delta=4.7569e-06)

        # Dens @ T=5degC, X=0.4: 1.0585e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0585e03, delta=1.0585e00)

        # SpHt @ T=5degC, X=0.4: 3.4559e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.4559e03, delta=3.4559e00)

        # Cond @ T=5degC, X=0.4: 4.1376e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.1376e-01, delta=4.1376e-04)

        # Visc @ T=20degC, X=0.4: 2.8191e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 2.8191e-03, delta=2.8191e-06)

        # Dens @ T=20degC, X=0.4: 1.0519e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0519e03, delta=1.0519e00)

        # SpHt @ T=20degC, X=0.4: 3.5190e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.5190e03, delta=3.5190e00)

        # Cond @ T=20degC, X=0.4: 4.2530e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.2530e-01, delta=4.2530e-04)

        # Visc @ T=40degC, X=0.4: 1.6351e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.6351e-03, delta=1.6351e-06)

        # Dens @ T=40degC, X=0.4: 1.0414e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0414e03, delta=1.0414e00)

        # SpHt @ T=40degC, X=0.4: 3.5978e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.5978e03, delta=3.5978e00)

        # Cond @ T=40degC, X=0.4: 4.4050e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 4.4050e-01, delta=4.4050e-04)

    def test_t_freeze(self):
        # T_freeze @ X=0.1: -3.357. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.1).freeze_point(0.1), -3.357, delta=1.0e-02)

        # T_freeze @ X=0.2: -7.949. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.2).freeze_point(0.2), -7.949, delta=1.0e-02)

        # T_freeze @ X=0.3: -14.576. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.3).freeze_point(0.3), -14.576, delta=1.0e-02)

        # T_freeze @ X=0.4: -23.813. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.4).freeze_point(0.4), -23.813, delta=1.0e-02)

        # T_freeze @ X=0.5: -35.994. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.5).freeze_point(0.5), -35.994, delta=1.0e-02)

        # T_freeze @ X=0.6: -51.201. ErrTol=0.01C
        self.assertAlmostEqual(EthyleneGlycol(0.6).freeze_point(0.6), -51.201, delta=1.0e-02)
