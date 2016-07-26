modele-tests
===============

This consists of unit tests for ModelE.  They are not part of the ModelE repo in order to simplify the build.  To build:

1. Configure your ModelE run directory using `ectl`.  For example:

.. code-block:: bash

    ectl setup ..path/to/rundir/e4f40 --rundeck ..path/to/templates/E4F40.R

2. Use `spack` to produce an `spconfig.py` files in `modele-tests`:

.. code-block:: bash

    spack setup modele-tests@local

3. Run CMake, using `ectl` to link to a built ModelE:

.. code-block:: bash

    mkdir build
    cd build
    ectl env ~/exp/160623-stieglitz/e4f40 ../spconfig.py ..

4. Inter-project connections are complete, now build like any other package:

.. code-block:: bash

    make
    make install    # If you really want to

5. Run the tests (the generated binaries)

