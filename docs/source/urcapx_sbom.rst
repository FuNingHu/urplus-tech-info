SBOM for a PolyScope X URCap
============================

.. note::
   **Published:** 2026-Nov-25 ·
   **Last Updated:** 2026-Nov-25 ·
   **Minimum PolyScope X version:** 10.14

.. raw:: html

   <p>An <a href="https://www.cisa.gov/sbom" target="_blank">SBOM</a> is the list of third-party components and their versions that are
   shipped in the URCap. For a PolyScope X URCap, generate that list from what
   runs on the robot. Do not scan the project folder or <code>node_modules</code>.</p>

What the built URCap contains
-----------------------------

The built URCap is the contents of the ``dist`` folder. ``package-urcap``
zips that folder into ``target/*.urcapx``.

``dist`` contains:

- the compiled frontend
- the backend image
- ``manifest.yaml``
- ``LICENSE``
- ``sbom.json``

Which package-lock.json to use
------------------------------

A URCap project has three ``package-lock.json`` files.

.. important::

   Use only the frontend lockfile for the runtime SBOM. Do not merge the three files.

Frontend
^^^^^^^^

``your-urcap-frontend/package-lock.json`` is the lockfile for the web
application shipped inside the URCap.

Production dependencies are compiled into the frontend bundle and belong on
the SBOM. Examples are Angular, rxjs, ngx-translate, and the Universal Robots
UI packages.

Build-only tools in that same file can be left out of the runtime SBOM, or
listed separately as build-only. Examples are the TypeScript compiler, ESLint,
and the Angular CLI.

Root project
^^^^^^^^^^^^

The ``package-lock.json`` in the root project directory lists only the
packaging tools used to assemble the URCap, such as
``@universal-robots/urcap-utils``. Those tools are not part of the URCap that
runs on the robot. Do not use this file for the runtime SBOM.

Backend directory
^^^^^^^^^^^^^^^^^

The ``package-lock.json`` in the backend directory has no application
dependencies. It only contains ``rimraf``, which deletes the build folder.
Do not use this file for the runtime SBOM.

The backend that runs on the robot is the Python image. Its third-party
components come from ``requirements.txt``, for example Flask, Werkzeug,
flask-cors, NumPy, and Shapely.

One document for everything shipped
-----------------------------------

If one document should cover everything shipped in the URCap, combine the
frontend production dependencies with the Python packages from
``requirements.txt``.

The SDK sbom.json
-----------------

While packaging, the SDK writes ``sbom.json`` from the frontend
``package-lock.json``. That file lists the ``@universal-robots`` packages
only. It is not a full CycloneDX document.

.. raw:: html

   <p>A security review may still ask for a
   <a href="https://cyclonedx.org/" target="_blank">CycloneDX</a>
   or SPDX document of the runtime dependencies. For a CycloneDX example,
   generate it from the frontend <code>package-lock.json</code> with
   development dependencies omitted, and add the Python packages from
   <code>requirements.txt</code>.</p>

.. admonition:: Info
   :class: note

   .. raw:: html

      <p><a href="https://cyclonedx.org/" target="_blank">CycloneDX</a> is a modern standard for the software supply chain.
      A CycloneDX bill of materials can represent a full-stack inventory of software, hardware,
      services, and other assets. The specification is led by the OWASP Foundation,
      standardized by Ecma International, and supported by the information security community.</p>
