from .water import Water
from .propylene_glycol import PropyleneGlycol
from .ethylene_glycol import EthyleneGlycol
from .methyl_alcohol import MethylAlcohol
from .ethyl_alcohol import EthylAlcohol

from .base_melinder import BaseMelinder
from typing import Any


class Fluid:

    fluids = {
        ('WATER',): Water,
        ('MPG', 'PROPYLENEGLYCOL'): PropyleneGlycol,
        ('MEG', 'ETHYLENEGLYCOL'): EthyleneGlycol,
        ('MMA', 'METHYLALCOHOL'): MethylAlcohol,
        ('ETHYLENEGLYCOL', 'MEA'): EthylAlcohol
    }

    @staticmethod
    def __new__(cls: Any, fluid_name: str, x: float = 0.0, *args: Any, **kwargs: Any) \
            -> BaseMelinder:

        for key in Fluid.fluids:
            if fluid_name.upper() in key:
                return Fluid.fluids[key](x=x)
        else:
            raise ValueError(f'Unsupported fluid mixture: "{fluid_name}".')
