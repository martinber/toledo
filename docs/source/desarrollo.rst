Desarrollo
==========

Acá va la información sobre el desarrollo de *toledo*.

Versión y changelog
-------------------

La versión está hardcodeada en:

- ``docs/source/cambios.rst``
- ``docs/source/index.rst``
- ``docs/source/conf.py``
- En una release de *GitHub*

El changelog está en:

- ``docs/source/cambios.rst``
- ``tests/test_0.X.py``
- En una release de *GitHub*

Documentación
-------------

Build
^^^^^
::
    cd docs
    make clean
    make html

Para publicar esto en *gh-pages* por primera vez, usé::

    git subtree push --prefix docs/build/html origin gh-pages
