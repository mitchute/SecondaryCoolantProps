from scp.base_melinder import BaseMelinder


class EthyleneGlycol(BaseMelinder):
    """
    A derived fluid class for ethylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a ethylene glycol mixture instance

        @param concentration: Glycol concentration, in percent, from 0.0 to 60.0
        """

        super().__init__(0, 100, concentration, 0.0, 60.0)
        self.t_min = self.t_freeze = self.calc_freeze_point(concentration)

        self.c_base = 30.8462
        self.t_base = 31.728

        self.coeff_visc = [
            [4.7050e-01, -2.5500e-02, 1.7820e-04, -7.6690e-07],
            [2.4710e-02, -1.1710e-04, 1.0520e-06, -1.6340e-08],
            [3.3280e-06, 1.0860e-06, 1.0510e-08, -6.4750e-10],
            [1.6590e-06, 3.1570e-09, 4.0630e-10, None],
            [3.0890e-08, 1.8310e-10, None, None],
            [-1.8650e-09, None, None, None],
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

    def calc_freeze_point(self, conc: float):
        """
        Calculate the freezing point temperature of the mixture

        Based on a curve fit of the Ethylene Glycol freezing points
        listed in Chapter 31, Table 4 of the ASHRAE Handbook of Fundamentals, 2009
        """

        # should return 0 C for low concentrations
        if conc < 0.05:
            return 0

        # polynomial fit
        # t_f = a + b * conc + c * conc**2 + d * conc**3
        conc = self._check_concentration(conc)
        coeff_freeze = [5.4792e-02, -2.9922e-01, -2.7478e-03, -9.5960e-05]
        c_pow = [conc**p for p in range(4)]
        return sum(x * y for x, y in zip(coeff_freeze, c_pow))

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "EthyleneGlycol"
        """
        return "EthyleneGlycol"

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        return self._f_prop(self.coeff_visc, temp)

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        return self._f_prop(self.coeff_spht, temp)

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        return self._f_prop(self.coeff_cond, temp)

    def density(self, temp: float) -> float:
        """
        Calculates the density of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        return self._f_prop(self.coeff_dens, temp)
