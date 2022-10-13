from scp.base_melinder import BaseMelinder
from scp.water import Water


class EthyleneGlycol(BaseMelinder):
    """
    A derived fluid class for ethylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a ethylene glycol mixture instance, taking the amount of concentration
        as the only argument

        @param concentration: Glycol concentration, in percent, from 0.0 to 60.0
        """

        # TODO: Update with freezing temperature
        t_min = 0.0
        super().__init__(t_min, 100, concentration, 0.0, 60.0)

        self.coeff_visc = [
            [4.7050e-04, -2.5500e-05, 1.7820e-07, -7.6690e-10],
            [2.4710e-05, -1.1710e-07, 1.0520e-09, -1.6340e-11],
            [3.3280e-09, 1.0860e-09, 1.0510e-11, -6.4750e-13],
            [1.6590e-09, 3.1570e-12, 4.0630e-13, None],
            [3.0890e-11, 1.8310e-13, None, None],
            [-1.8650e-12, None, None, None],
        ]

        self.coeff_spht = [
            [3.7370e03, 2.9300e00, -4.6750e-03, -1.3890e-05],
            [-1.7990e01, 1.0460e-01, -4.1470e-04, 1.8470e-7],
            [-9.9330e-02, 3.5160e-04, 5.1090e-06, -7.1380e-08],
            [2.6100e-03, -1.1890e-06, -1.6430e-7, None],
            [1.5370e-05, -4.2720e-07, None, None],
            [-1.6180e-06, None, None, None],
        ]

        self.coeff_cond = [
            [4.7200e-01, 8.9030e-04, -1.0580e-06, -2.7890e-09],
            [-4.2860e-03, -1.4730e-05, 1.0590e-07, -1.1420e-10],
            [1.7470e-05, 6.8140e-08, -3.6120e-09, 2.3650e-12],
            [3.0170e-08, -2.4120e-09, 4.0040e-11, None],
            [-1.3220e-09, 2.5550e-11, None, None],
            [2.6780e-11, None, None, None],
        ]

        self.coeff_dens = [
            [1.0340e03, -4.7810e-01, -2.6920e-03, 4.7250e-06],
            [1.3110e00, -6.8760e-03, 4.8050e-05, 1.6900e-08],
            [7.4900e-05, 7.8550e-05, -3.9950e-07, 4.9820e-09],
            [-1.0620e-04, 1.2290e-06, -1.1530e-08, None],
            [-9.6230e-07, -7.2110e-08, None, None],
            [4.8910e-08, None, None, None],
        ]

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "EthyleneGlycol"
        """
        return "EthyleneGlycol"

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        return self._f_prop(self.coeff_visc, temp)

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        return self._f_prop(self.coeff_spht, temp)

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        return self._f_prop(self.coeff_cond, temp)

    def density(self, temp: float) -> float:
        """
        Calculates the density of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        return self._f_prop(self.coeff_dens, temp)
