from .water import Water
from .propylene_glycol import PropyleneGlycol
from .ethylene_glycol import EthyleneGlycol
from .methyl_alcohol import MethylAlcohol
from .ethyl_alcohol import EthylAlcohol

from .base_fluid import BaseFluid
from .base_melinder import BaseMelinder
from typing import Any, Union

from sys import stderr


class Fluid:

    fluids = {
        ('water', 'WATER'): Water,
        ('propylene_glycol', 'PROPYLENEGLYCOL', 'MPG'): PropyleneGlycol,
        ('ethylene_glycol', 'ETHYLENEGLYCOL', 'MEG'): EthyleneGlycol,
        ('methyl_alcohol', 'METHYLALCOHOL', 'MMA'): MethylAlcohol,
        ('ethylene_glycol', 'ETHYLENEGLYCOL', 'MEA'): EthylAlcohol
    }

    @staticmethod
    def __new__(cls: Any, fluid_name: str, x: float = 0.0, *args: Any, **kwargs: Any) \
            -> Union[BaseFluid, BaseMelinder]:

        for key in Fluid.fluids:
            if fluid_name.upper() in key:
                fluid_cls = Fluid.fluids[key]
                if type(fluid_cls) != Water and x == 0.0:
                    print("Mixture requested, but concentration zero, assuming "
                          "water and continuing.", file=stderr)
                    fluid_cls = Water
                return fluid_cls(x=x)
        else:
            raise ValueError(f'Unsupported fluid mixture: "{fluid_name}".')
