======
Readme
======

This repo contains the latest version of my CV. I am maintaining it
with the reStructuredText (ReST) syntax - an easy-to-read markup
language that can easily be compiled to both PDF and HTML.


To generate cv.pdf
==================

.. code-block:: bash

    rst2pdf cv.txt cv.pdf -s cv.style

To generate cv.html
===================

.. code-block:: bash

    rst2html.py cv.txt cv.html --stylesheet cv.css
