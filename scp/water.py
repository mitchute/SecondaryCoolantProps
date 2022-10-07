from typing import Union

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

    def viscosity(self, temp: Union[int, float]) -> float:
        """
        Returns the fluid viscosity for this derived fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Viscosity (WHICH ONE?) in UNITS
        """
        return BaseFluid._viscosity_water(temp)

    def specific_heat(self, temp: Union[int, float]) -> float:
        """
        Returns the fluid specific heat for this derived fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Specific heat, in J/kg-K ???
        """
        return -999.0

    def conductivity(self, temp: Union[int, float]) -> float:
        """
        Returns the fluid thermal conductivity for this derived fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Thermal conductivity, in W/m-K ???
        """
        return -999.0

    def density(self, temp: Union[int, float]) -> float:
        """
        Returns the fluid density for this derived fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Density, in kg/m3 ???
        """
        return -999.0
