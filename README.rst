======
Readme
======

This repo contains the latest version of my CV. I am maintaining it
with the reStructuredText (ReST) syntax - an easy-to-read markup
language that can easily be compiled to both PDF and HTML.


To generate PDF
===============

.. code-block:: bash

    rst2pdf cv.txt OscarByrneCV.pdf -s cv.style

To generate HTML
================

.. code-block:: bash

    rst2html.py cv.txt index.html --stylesheet cv.css
