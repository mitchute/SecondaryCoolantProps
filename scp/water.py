from typing import Union
from math import exp, log10
from scp.base_fluid import BaseFluid


class Water(BaseFluid):
    def __init__(self, concentration: Union[int, float] = 0) -> None:
        super().__init__(concentration)

    def viscosity(self, temperature: Union[int, float] = 0):
        return BaseFluid._viscosity_water(temperature)

    def specific_heat(self, temperature: Union[int, float] = 0):
        pass

    def conductivity(self, temperature: Union[int, float] = 0):
        pass

    def density(self, temperature: Union[int, float] = 0):
        pass
