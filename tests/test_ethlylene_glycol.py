from unittest import TestCase

from scp.ethylene_glycol import EthyleneGlycol


class TestEthyleneGlycol(TestCase):

    def test_1(self):

        p = EthyleneGlycol(0.0)

        # Visc @ T=5degC, X=0: 1.5186e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 1.5186e-03, delta=1.5186e-06)

        # Dens @ T=5degC, X=0: 9.9915e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 9.9915e+02, delta=9.9915e-01)

        # SpHt @ T=5degC, X=0: 4.2027e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 4.2027e+03, delta=4.2027e+00)

        # Cond @ T=5degC, X=0: 5.7137e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 5.7137e-01, delta=5.7137e-04)

        # Visc @ T=20degC, X=0: 1.0078e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.0078e-03, delta=1.0078e-06)

        # Dens @ T=20degC, X=0: 9.9735e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 9.9735e+02, delta=9.9735e-01)

        # SpHt @ T=20degC, X=0: 4.1862e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 4.1862e+03, delta=4.1862e+00)

        # Cond @ T=20degC, X=0: 5.9913e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.9913e-01, delta=5.9913e-04)

        # Visc @ T=40degC, X=0: 6.5721e-04. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 6.5721e-04, delta=6.5721e-07)

        # Dens @ T=40degC, X=0: 9.9181e+02. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 9.9181e+02, delta=9.9181e-01)

        # SpHt @ T=40degC, X=0: 4.1785e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 4.1785e+03, delta=4.1785e+00)

        # Cond @ T=40degC, X=0: 6.2983e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 6.2983e-01, delta=6.2983e-04)

    def test_2(self):

        p = EthyleneGlycol(20.0)

        # Visc @ T=5degC, X=20: 2.6594e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 2.6594e-03, delta=2.6594e-06)

        # Dens @ T=5degC, X=20: 1.0281e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0281e+03, delta=1.0281e+00)

        # SpHt @ T=5degC, X=20: 3.8695e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.8695e+03, delta=3.8695e+00)

        # Cond @ T=5degC, X=20: 4.9022e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.9022e-01, delta=4.9022e-04)

        # Visc @ T=20degC, X=20: 1.6624e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 1.6624e-03, delta=1.6624e-06)

        # Dens @ T=20degC, X=20: 1.0241e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0241e+03, delta=1.0241e+00)

        # SpHt @ T=20degC, X=20: 3.8962e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.8962e+03, delta=3.8962e+00)

        # Cond @ T=20degC, X=20: 5.0766e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 5.0766e-01, delta=5.0766e-04)

        # Visc @ T=40degC, X=20: 1.0133e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.0133e-03, delta=1.0133e-06)

        # Dens @ T=40degC, X=20: 1.0164e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0164e+03, delta=1.0164e+00)

        # SpHt @ T=40degC, X=20: 3.9328e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.9328e+03, delta=3.9328e+00)

        # Cond @ T=40degC, X=20: 5.2908e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 5.2908e-01, delta=5.2908e-04)

    def test_3(self):

        p = EthyleneGlycol(40.0)

        # Visc @ T=5degC, X=40: 4.7569e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(5), 4.7569e-03, delta=4.7569e-06)

        # Dens @ T=5degC, X=40: 1.0585e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(5), 1.0585e+03, delta=1.0585e+00)

        # SpHt @ T=5degC, X=40: 3.4559e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(5), 3.4559e+03, delta=3.4559e+00)

        # Cond @ T=5degC, X=40: 4.1376e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(5), 4.1376e-01, delta=4.1376e-04)

        # Visc @ T=20degC, X=40: 2.8191e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(20), 2.8191e-03, delta=2.8191e-06)

        # Dens @ T=20degC, X=40: 1.0519e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(20), 1.0519e+03, delta=1.0519e+00)

        # SpHt @ T=20degC, X=40: 3.5190e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(20), 3.5190e+03, delta=3.5190e+00)

        # Cond @ T=20degC, X=40: 4.2530e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(20), 4.2530e-01, delta=4.2530e-04)

        # Visc @ T=40degC, X=40: 1.6351e-03. Err Tol: 0.1%
        self.assertAlmostEqual(p.viscosity(40), 1.6351e-03, delta=1.6351e-06)

        # Dens @ T=40degC, X=40: 1.0414e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.density(40), 1.0414e+03, delta=1.0414e+00)

        # SpHt @ T=40degC, X=40: 3.5978e+03. Err Tol: 0.1%
        self.assertAlmostEqual(p.specific_heat(40), 3.5978e+03, delta=3.5978e+00)

        # Cond @ T=40degC, X=40: 4.4050e-01. Err Tol: 0.1%
        self.assertAlmostEqual(p.conductivity(40), 4.4050e-01, delta=4.4050e-04)
