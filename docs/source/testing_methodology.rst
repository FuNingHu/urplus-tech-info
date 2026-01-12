Testing Methodology
===================

This section describes the testing and validation procedures for UR+ products.

Overview
--------

The UR+ Tech Team will test the product using **UAT (User Acceptance Testing)**. This type
of analysis is the last phase of any testing process and verifies that the product can
handle required tasks in real-world scenarios, according to the scope and specifications.

Using only the provided BOM, product documentation, and URCap, the UR+ Tech Responsible
will attempt to set up the product and implement a robot application while checking for
expected behavior, and impedance to the robot's functionality.

To ensure that use of the product does not require prerequisite skills, the target audience
emulated in this test is an **inexperienced novice user**.

During this test, issues found will be grouped into 4 different severities. These categories,
and the subsequent actions required from the UR+ partners can be found below.

Issue Severity Categories
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 20 35 30

   * - Category
     - Approved Status
     - Definition
     - Action Item
   * - **Critical**
     - Does not qualify for approval
     - The issue found has a major impact on the general product, or on the robot's
       functionality.
     - A new retest is required when the issue is corrected.
   * - **Must-fix**
     - Does not qualify for approval
     - The issue found is a major or limited bug that has limited impact on the product
       or robot. Only certain sections of the test that use this part will need verification.
     - A limited verification is required when the issue is corrected.
   * - **Should-fix**
     - May qualifies for approval
     - The issue found is less severe, and results in a less optimal user experience,
       or limits possible uses.
     - Notice of correction is required, no retest or verification needed.
   * - **Suggestion**
     - Qualifies for approval
     - These are suggestions that the UR+ team has that can improve the product's
       attractiveness in the UR+ ecosystem.
     - Suggestions made are optional for the partner.

The results of the test performed by UR, and the ensuing findings, will be provided to
the partner through a test report. Prior to the product test, the development team should
ensure that each item in the pre-test checklist (see Appendix) has been accounted for.


Testing Methods
---------------

Dependent on the product, timeline and other circumstances, testing can be performed in
the following ways:

* **UR Office:** The product is shipped to a UR office for hands-on testing
* **OnSite:** A UR colleague visits the partner site to conduct testing
* **Remote:** The product/system is set up at the partner location and testing is
  performed remotely

Partner Self-Testing
--------------------

Before submitting for UR+ certification, partners are recommended to complete internal
testing using the self-testing checklist provided in the appendix. This helps ensure
readiness for the formal testing procedure.

Key areas to verify:

* **Hardware:** Scope of delivery includes all basic materials to operate the product
* **Software:** URCap meta information is complete and professional
* **Documentation:** User manual covers all necessary configuration and specifications
* **Launching preparation:** Product landing page and marketing materials are ready

.. note::
   The self-testing checklist should be used as a reference to ensure readiness for
   the testing procedure. Completing self-testing thoroughly can significantly reduce
   the number of retesting sessions required.

Retesting
---------

Depending on the outcome of the initial testing, there may be the need for one or more
retesting sessions. Partners should:

1. Address all **Blocker** and **Major** issues before requesting retesting
2. Document all changes made to resolve identified issues
3. Update documentation to reflect any modifications
4. Coordinate with UR+ Development Consultant to schedule retesting

.. warning::
   Products with unresolved Blocker issues cannot proceed to approval. Ensure all
   critical issues are addressed before requesting retesting.
