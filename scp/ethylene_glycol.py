from math import exp, log

from scp.base import BaseFluid
from scp.water import Water


class EthyleneGlycol(BaseFluid):
    """
    A derived fluid class for ethylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a ethylene glycol mixture instance, taking the amount of concentration
        as the only argument

        @param concentration: Glycol concentration, from 0.0 to 100.0
        """
        super().__init__(concentration)
        self.water = Water()
        self._set_concentration_limits(0.0, 0.6)

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "EthyleneGlycol"
        """
        return "EthyleneGlycol"

    def _viscosity_eg(self, temp: float) -> float:
        """
        Internal worker function that can give the viscosity of pure ethylene glycol.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Viscosity something
        """

        self._check_temperature(temp)

        return exp(-16.548 + (3022.7 / (temp + 273.15)) + 0.08248 * log((temp + 273.15)))

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        self._check_temperature(temp)

        return 0.0016624202

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        self._check_temperature(temp)

        return 3896.19

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        self._check_temperature(temp)

        return 0.5076

    def density(self, temp: float) -> float:
        """
        Calculates the density of this Ethylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        self._check_temperature(temp)

        return 1024.10
