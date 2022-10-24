Propylene Glycol
================

Provides fluid properties for aqueous mixtures of Propylene Gycol for temperatures <=100 C, with concentrations from 0-0.6.

Example::

    from scp.propylene_glycol import PropyleneGycol

    if __name__ == "__main__":
        x_fraction = 0.2  # concentration fraction
        pg = PropyleneGycol(x_fraction)

        temp = 10  # Celsius
        print(pg.viscosity(temp))

.. automodule:: scp.propylene_glycol
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
