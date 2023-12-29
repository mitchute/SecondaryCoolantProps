import numpy as np

from scp.propylene_glycol import PropyleneGlycol


def test_0_per():
    p = PropyleneGlycol(0.0)

    np.testing.assert_almost_equal(p.viscosity([5, 20, 40]), [1.5364e-03, 1.0072e-03, 6.5033e-04], decimal=1)
    np.testing.assert_almost_equal(p.density([5, 20, 40]), [1.0003e03, 9.9852e02, 9.9253e02], decimal=1)
    np.testing.assert_almost_equal(p.specific_heat([5, 20, 40]), [4.2048e03, 4.1866e03, 4.1783e03], decimal=1)
    np.testing.assert_almost_equal(p.conductivity([5, 20, 40]), [5.7124e-01, 5.9913e-01, 6.3007e-01], decimal=1)

    list_of_temperatures = [5, 20, 40]

    np.testing.assert_almost_equal(p.viscosity(list_of_temperatures), [p.viscosity(i) for i in list_of_temperatures], decimal=6)
    np.testing.assert_almost_equal(p.density(list_of_temperatures), [p.density(i) for i in list_of_temperatures], decimal=6)
    np.testing.assert_almost_equal(p.specific_heat(list_of_temperatures), [p.specific_heat(i) for i in list_of_temperatures], decimal=6)
    np.testing.assert_almost_equal(p.conductivity(list_of_temperatures), [p.conductivity(i) for i in list_of_temperatures], decimal=6)


def test_20_per():
    p = PropyleneGlycol(0.2)
    list_of_concentration = [5, 20, 40]

    np.testing.assert_almost_equal(p.viscosity(list_of_concentration), [p.viscosity(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.density(list_of_concentration), [p.density(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.specific_heat(list_of_concentration),
                                   [p.specific_heat(i) for i in list_of_concentration], decimal=1)
    np.testing.assert_almost_equal(p.conductivity(list_of_concentration),
                                   [p.conductivity(i) for i in list_of_concentration], decimal=1)


def test_40_per():
    p = PropyleneGlycol(0.4)
    list_of_concentration = [5, 20, 40]

    np.testing.assert_almost_equal(p.viscosity(list_of_concentration), [p.viscosity(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.density(list_of_concentration), [p.density(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.specific_heat(list_of_concentration),
                                   [p.specific_heat(i) for i in list_of_concentration], decimal=1)
    np.testing.assert_almost_equal(p.conductivity(list_of_concentration),
                                   [p.conductivity(i) for i in list_of_concentration], decimal=1)


def test_60_per():
    p = PropyleneGlycol(0.6)
    list_of_concentration = [5, 20, 40]

    np.testing.assert_almost_equal(p.viscosity(list_of_concentration), [p.viscosity(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.density(list_of_concentration), [p.density(i) for i in list_of_concentration],
                                   decimal=1)
    np.testing.assert_almost_equal(p.specific_heat(list_of_concentration),
                                   [p.specific_heat(i) for i in list_of_concentration], decimal=1)
    np.testing.assert_almost_equal(p.conductivity(list_of_concentration),
                                   [p.conductivity(i) for i in list_of_concentration], decimal=1)

test_0_per()