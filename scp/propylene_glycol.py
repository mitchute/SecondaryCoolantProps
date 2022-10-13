from math import exp, log

from scp.base_fluid import BaseFluid
from scp.water import Water


class PropyleneGlycol(BaseFluid):
    """
    A derived fluid class for propylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a propylene glycol mixture instance, taking the amount of concentration
        as the only argument

        @param concentration: Glycol concentration, in percent, from 0.0 to 60.0
        """

        # TODO: Update with freezing temperature
        t_min = 0.0
        super().__init__(t_min, 100, concentration, 0.0, 60.0)

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "PropyleneGlycol"
        """
        return "PropyleneGlycol"

    def _viscosity_pg(self, temp: float) -> float:
        """
        Internal worker function that can give the viscosity of pure propylene glycol.
        These doc strings should have citations I think.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity [Pa s]
        """

        temp = self._check_temperature(temp)

        return exp(-293.07 + (17494 / (temp + 273.15)) + 40.576 * log((temp + 273.15)))

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        temp = self._check_temperature(temp)

        # 20C, 20%
        return 0.0020300812

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        temp = self._check_temperature(temp)

        # 20C, 20%
        return 3976.76

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        temp = self._check_temperature(temp)

        # 20C, 20%
        return 0.4922

    def density(self, temp: float) -> float:
        """
        Calculates the density of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        temp = self._check_temperature(temp)

        # 20C, 20%
        return 1014.77
