Development Deliverables
========================

This section outlines the required deliverables for UR+ product certification.

Overview
--------

Partners must provide a complete set of deliverables to ensure their product meets UR+ standards and can be properly evaluated for certification.

Deliverables by Product Type
----------------------------

.. list-table:: 
   :header-rows: 1
   :widths: 18 41 41
   :class: tight-table

   * - Deliverable
     - UR+ Component
     - UR+ Application Kit
   * - **Hardware**
     - This is the main deliverable and should be presented in the way an end user can expect to receive the product. This will include your product, any external parts, mounting hardware and tools, and electrical components and tools. The end user should not need any extra equipment to set up the product.
     - This is the main deliverable and should contain all the subcomponents listed in the scope of the application kit. Each subcomponent, and the overall kit should contain all necessary equipment and parts to set up the kit.
   * - **Software**
     - If a URCap is required for product integration, this must be aligned with the UR+ team during the scoping phase. In such cases, the URCap should be made easily accessible to users—either via online download or provided on a USB stick and included in the Bill of Materials (BOM). Any external software necessary for product operation must also be provided in the same manner. If no URCap is provided, the product must still include all necessary resources to ensure a seamless integration and deployment experience. This includes sample programs, URScript code, coniguration modules. 
     - All URCaps used in the UR+ application kit must be provided. Any additional software needed must also be provided to the user. If the URCaps or external software is not available for easy download, it must be provided through a USB stick and added to the BOM. Hardware required to interface from the external software to the robot must also be included. If no URCap is provided, the product must still include all necessary resources to ensure a seamless integration and deployment experience. This includes sample programs, URScript code, configuration modules.
   * - **Documentation** (Common)
     - All UR+ Products must include a UR specific user manual that guides users through mechanical and electrical setup of the product on the robot, as well as information on the installation and navigation of the URCap and its functions. The user manual must also include the BOM. Include any relevant internal testing documentation, third party approval reports, product specific manuals, and documentation of product design choices.
     - *(Same as UR+ Component)*
   * - **Documentation** (Specific)
     - The manual should have version table exposing detailed change log for easy of change tracking. It is recommended to follow a version definition approach of Major.Minor-Patch format. In case the product is released in multi-region, partner should prepare local languages manual prior to the release.
     - UR+ Kits must include a UR specific user manual to guide users through installation and navigating through URCap functions. There can be individual manuals for each subcomponent of the UR+ Application Kit.
   * - **Release Materials**
     - UR+ product launching requires partner to get below items ready and easy to access for end user: 1) Landing product page hosted on Partner's website, exclusive to showcase product introduction, pictures, URCap (optional), manual (optional). 2) 2-4 high resolution product images for UR MarketPlace gallery. 3) 2-3 pictures of software/URCap UI. 4) Logo picture.
     - Same requirements as UR+ Component.
   * - **Testing Artifacts**
     - Some UR+ testing may require separate components that can assist or aid in the approval of the product. These parts must be packed or labeled separately, to distinguish between "the product" and assistive parts.
     - Some UR+ testing may require separate components that can assist or aid in the approval of the product. These parts must be packed or labeled separately, to distinguish between "the product" and assistive parts.

Documentation Requirements
--------------------------

The user manual should cover, but not limited to:

1. Cobot TCP (Tool Center Point) configuration
2. Cobot mounting configuration
3. Cobot payload settings
4. Tool-IO configuration
5. Safety IO / Plan configuration (if applicable)
6. Others

The manual needs to cover product key specifications:

1. Product weight
2. Product power (rated, peak, range)
3. Product cleanroom level
4. Product stroke (applies to external axis)
5. Maximum velocity (applies to external axis)
6. Maximum force (applies to gripper)
7. Dependencies (if applicable)

.. note::
   The manual should have a version table exposing detailed change log for ease of change tracking. It is recommended to follow a version definition approach of **Major.Minor-Patch** format. In case the product is released in multi-region, partner should prepare local language manuals prior to the release.

Submission Format
-----------------

* All documents in PDF format
* Source files in editable format (Word, InDesign, etc.)
* Software packages with version numbers
* Organized folder structure

.. warning::
   Incomplete deliverables will delay the certification process. Ensure all items are ready before submission.

Version Control
---------------

Partners must maintain version control for all deliverables:

* Use semantic versioning (e.g., 1.0.0)
* Document changes between versions
* Maintain compatibility matrix with PolyScope versions
