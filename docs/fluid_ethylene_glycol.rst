Ethylene Glycol
===============

Provides fluid properties for aqueous mixtures of Ethylene Glycol for temperatures <= 100 C, with concentrations from 0-0.6.

Example::

    from scp.ethylene_glycol import EthyleneGlycol

    if __name__ == "__main__":
        x_fraction = 0.2  # concentration fraction
        eg = EthyleneGlycol(x_fraction)

        temp = 10  # Celsius
        print(eg.viscosity(temp))

.. automodule:: scp.ethylene_glycol
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
