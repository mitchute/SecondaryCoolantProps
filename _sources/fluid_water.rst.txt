Water
=====

Provides fluid properties for liquid water between 0-100 C.

Example::

    from scp.water import Water

    if __name__ == "__main__":
        water = Water()
        temp = 10  # Celsius
        print(water.viscosity(temp))

.. automodule:: scp.water
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
