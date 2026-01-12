Self-Testing Checkpoint
=======================

This section outlines the self-testing checklist for UR+ product development. Prior to the
product test, the development team should ensure that each item in this checklist has been
accounted for.

Hardware Checklist
------------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Checkpoint
     - Motivation
   * - Is the scope of delivery defined in a way to include all basic materials to operate
       the product?
     - Quick setup
   * - If applicable, is supplemental equipment included like adapters, screws etc.?
     - Quick setup
   * - Is it clear to the customer what additional components or tools may be required to
       use the product?
     - Quick setup

Software Checklist
------------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Checkpoint
     - Motivation
   * - The URCaps meta information needs to be complete, and does not include phrases like
       'sample', 'example', 'trial', 'snapshot'
     - Product commercialization
   * - License information has been specified.
     - Product commercialization
   * - Value in input field are to be checking the validity, i.e, range check, type check,
       length check.
     - For value input correctness checking
   * - Relevant values are being stored in the correspondent node. The saveNode() method is
       being called every time those values are changed. This allows the node to display
       the URCap nodes settings correctly.
     - For value being able to safely store in node. If storing correctly every component
       can properly display its own value when switching between them.
   * - In case a websocket port is claimed through manifest.yaml file via the exposePorts
       parameter, it needs to explicitly claimed and reserved through the forum and included
       in the manual.
     - Ensuring URCap compatibility
   * - In case a shared variable is being used, it needs to be explicitly exposed in user
       manual for compatibility check in application with other URCaps.
     - Ensure URCap compatibility
   * - Global variables, shared variables, handles (xmlrpc, ethernet/ip) need to be named
       in a customized way: ``vendorid_productid_varname``. Examples:
       
       • ``global smc_lehr_timer``
       
       • ``shared aspina_305_counter``
       
       • ``global rpc_daemon``
     - Ensure URCap compatibility
   * - Program nodes are calling a function defined in the application node instead of
       adding the full correspondent URScript code with each node.
     - Reduces program size and improves debugging

Documentation Checklist
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Checkpoint
     - Motivation
   * - User manual covers mechanical and electrical setup of the product on the robot.
     - Complete documentation
   * - User manual includes installation and navigation of the URCap and its functions.
     - Complete documentation
   * - Bill of Materials (BOM) is included in the user manual.
     - Complete documentation
   * - Version table with change log is included in the manual.
     - Easy tracking of changes

Launching Preparation Checklist
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Checkpoint
     - Motivation
   * - Product landing page does NOT contain 3rd party robot brand.
     - Ensure the focused synergy with co-marketing effort
   * - Product pictures are prepared (2-4 high resolution images).
     - Onboard Marketplace page requirement
   * - Software/URCap UI snapshots are prepared (2-3 pictures).
     - Onboard Marketplace page requirement
   * - In case the product is available globally / in a variation of countries, the relevant
       resources are translated.
     - Better traction locally

.. note::
   Completing this self-testing checklist thoroughly before submitting for UR+ certification
   can significantly reduce the number of retesting sessions required.
