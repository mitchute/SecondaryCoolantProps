Methyl Alcohol (Methylene)
==========================

Provides fluid properties for aqueous mixtures of Methylene for temperatures <= 40 C, with concentrations from 0-0.6.

Example::

    from scp.methyl_alcohol import MethylAlcohol

    if __name__ == "__main__":
        x_fraction = 0.2  # concentration fraction
        ma = MethylAlcohol(x_fraction)

        temp = 10  # Celsius
        print(ma.viscosity(temp))

.. automodule:: scp.methyl_alcohol
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
