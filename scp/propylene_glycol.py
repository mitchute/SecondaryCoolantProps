from scp.base_melinder import BaseMelinder


class PropyleneGlycol(BaseMelinder):
    """
    A derived fluid class for propylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a propylene glycol mixture instance

        @param concentration: Glycol concentration, in percent, from 0.0 to 60.0
        """

        super().__init__(0.0, 100.0, concentration, 0.0, 60.0)
        self.t_min = self.t_freeze = self.calc_freeze_point(concentration)

        self.c_base = 30.7031
        self.t_base = 32.7083

        self.coeff_visc = [
            [6.8370e-01, -3.0450e-02, 2.5250e-04, -1.3990e-06],
            [3.3280e-02, -3.9840e-04, 4.3320e-06, -1.8600e-08],
            [5.4530e-05, -8.6000e-08, -1.5930e-08, -4.4650e-11],
            [-3.9000e-06, 1.0540e-07, -1.5890e-09],
            [-1.5870e-08, 4.4750e-10],
            [3.5640e-09],
        ]

        self.coeff_spht = [
            [3.8820e03, 2.6990e00, -1.6590e-03, -1.0320e-05],
            [-1.3040e01, 5.0700e-02, -4.7520e-05, 1.5220e-06],
            [-1.5980e-01, 9.5340e-05, 1.1670e-05, -4.8700e-08],
            [3.5390e-04, 3.1020e-05, -2.9500e-07],
            [5.0000e-05, -7.1350e-07],
            [-4.9590e-07],
        ]

        self.coeff_cond = [
            [4.5130e-01, 7.9550e-04, 3.4820e-08, -5.9660e-09],
            [-4.7950e-03, -1.6780e-05, 8.9410e-08, 1.4930e-10],
            [2.0760e-05, 1.5630e-07, -4.6150e-09, 9.8970e-12],
            [-9.0830e-08, -2.5180e-09, 6.5430e-11],
            [-5.9520e-10, -3.6050e-11],
            [2.1040e-11],
        ]

        self.coeff_dens = [
            [1.0180e03, -5.4060e-01, -2.6660e-03, 1.3470e-05],
            [7.6040e-01, -9.4500e-03, 5.5410e-05, -1.3430e-07],
            [-2.4980e-03, 2.7000e-05, -4.0180e-07, 3.3760e-09],
            [-1.5500e-04, 2.8290e-06, -7.1750e-09],
            [-1.1310e-06, -2.2210e-08],
            [2.3420e-08],
        ]

    def calc_freeze_point(self, conc: float):
        """
        Calculate the freezing point temperature of the mixture

        Based on a curve fit of the Propylene Glycol freezing points
        listed in Chapter 31, Table 4 of the ASHRAE Handbook of Fundamentals, 2009
        """

        # should return 0 C for low concentrations
        if conc < 0.05:
            return 0

        # polynomial fit
        # t_f = a + b * conc + c * conc**2 + d * conc**3
        conc = self._check_concentration(conc)
        coeff_freeze = [7.1734e-03, -3.3692e-01, 2.8466e-03, -1.9024e-04]
        c_pow = [conc**p for p in range(4)]
        return sum(x * y for x, y in zip(coeff_freeze, c_pow))

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "PropyleneGlycol"
        """
        return "PropyleneGlycol"

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
