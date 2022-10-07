from typing import Union

from scp.base_fluid import BaseFluid


class Water(BaseFluid):
    def __init__(self, concentration: Union[int, float] = 0) -> None:
        super().__init__(concentration)

    def viscosity(self, temp: Union[int, float] = 0):
        return BaseFluid._viscosity_water(temp)

    def specific_heat(self, temp: Union[int, float] = 0):
        pass

    def conductivity(self, temp: Union[int, float] = 0):
        pass

    def density(self, temp: Union[int, float] = 0):
        pass
