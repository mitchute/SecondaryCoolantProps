Ethyl Alcohol (Ethylene)
========================

Provides fluid properties for aqueous mixtures of Ethylene for temperatures <= 40 C, with concentrations from 0-0.6.

Example::

    from scp.ethyl_alcohol import MethylAlcohol

    if __name__ == "__main__":
        x_fraction = 0.2  # concentration fraction
        ea = EthylAlcohol(x_fraction)

        temp = 10  # Celsius
        print(ea.viscosity(temp))

.. automodule:: scp.ethyl_alcohol
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
