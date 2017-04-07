Desarrollo
==========

Acá va la información sobre el desarrollo de *toledo*.

Versión y changelog
-------------------

El número de versión está hardcodeado en:

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

Build::

    cd docs
    make clean
    make html
    cd ..
    git subtree push --prefix docs/build/html origin gh-pages
