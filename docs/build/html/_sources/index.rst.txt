.. toledo documentation master file, created by
   sphinx-quickstart on Tue Apr  4 00:18:11 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentación de toledo!
========================

En este sitio está toda la documentación, acá está el `repositorio`_ (código fuente).

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   toledo
   cambios
   desarrollo

- :ref:`genindex`

Introducción
============

Este es un framework, que es algo así como un conjunto de cosas (funciones,
objetos) que tienen todo lo que haga falta para hacer un juego.

En vez de usar **pygame** directamente, uno usa a **toledo**. **toledo** se
encarga de hacer todo (a escondidas usa **pygame** pero no te importa).

Lo hago porque a veces **pygame** es difícil de usar o porque le faltan cosas.

Actualmente la versión es **toledo 0.2.6**. Acuérdense de actualizarse!.

Cómo aprender?
==============

Ver los ejemplos en la carpeta `tests`. Hay un ejemplo para las novedades de
cada versión de toledo.

Después mirar esta documentación. Está explicada cada función y clase, algunas
tienen ejemplos también.

Notas
=====

- Por ahora antes de correr los ejemplos hay que hacer `cd` a la carpeta.
- Para poder escalar/rotar imágenes con antialiasing, las imágenes deben ser de
  32 o 34 bits.
- No dibujen imágenes rotadas **y** escaladas negativamente **con** anclaje
  top-left. Esa combinación no anda, pero pueden hacer esas cosas por separado
  o dos de esas cosas al mismo tiempo, pero las tres juntas no. Es porque no
  me puse a hacer la matemática para ese caso.
- Tenemos problemas de stuttering culpa de `pygame`/`sdl`. Si uso otro método
  gasto mucha CPU, por ahora lo dejo así.
- Los sprites vibran mucho cuando son rotados debido a redondeos, no sé como
  solucionar eso.


.. _repositorio: https://github.com/toboso-team/toledo
