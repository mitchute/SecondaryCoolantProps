from scp.base import BaseFluid


class Water(BaseFluid):
    def __init__(self) -> None:
        """
        This class represents water as a fluid.  The constructor
        does not require any arguments for the pure water fluid.
        """
        super().__init__(0.0)

    def fluid_name(self) -> str:
        """
        Returns the fluid name for this derived fluid.

        :return: "Water"
        """
        return "Water"

    def viscosity(self, temp: float) -> float:
        """
        Returns the viscosity of water.

        :param temp: Fluid temperature, in degrees Celsius
        :return: The dynamic viscosity of water in [Pa s]
        """

        self._check_temperature(temp)

        am0 = -3.30233
        am1 = 1301
        am2 = 998.333
        am3 = 8.1855
        am4 = 0.00585
        am5 = 1.002
        am6 = -1.3272
        am7 = -0.001053
        am8 = 105
        am10 = 0.68714
        am11 = -0.0059231
        am12 = 2.1249e-05
        am13 = -2.69575e-08
        if temp < 20:
            exponent = (am0 + am1 / (am2 + (temp - 20) * (am3 + am4 * (temp - 20))))
            return (10 ** exponent) * 0.1
        if temp > 100:
            return (am10 + temp * am11 + (temp ** 2) * am12 + (temp ** 3) * am13) * 0.001
        return (am5 * 10 ** ((temp - 20) * (am6 + (temp - 20) * am7) / (temp + am8))) * 0.001

    def specific_heat(self, temp: float) -> float:
        """
        Returns the fluid specific heat for this derived fluid.

        :param temp: Fluid temperature, in degrees Celsius
        :return: Specific heat, in J/kg-K ???
        """

        self._check_temperature(temp)

        return -999.0

    def conductivity(self, temp: float) -> float:
        """
        Returns the fluid thermal conductivity for this derived fluid.

        :param temp: Fluid temperature, in degrees Celsius
        :return: Thermal conductivity, in W/m-K ???
        """

        self._check_temperature(temp)

        return -999.0

    def density(self, temp: float) -> float:
        """
        Returns the fluid density for this derived fluid.

        :param temp: Fluid temperature, in degrees Celsius
        :return: Density, in kg/m3 ???
        """

        self._check_temperature(temp)

        return -999.0
