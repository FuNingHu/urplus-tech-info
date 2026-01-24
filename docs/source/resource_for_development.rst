Resources for Development
=========================

Universal Robots provides a range of resources to support development. The following list is a summary of 
the most prominent sites to visit.

Community Resources
-------------------

.. raw:: html

   <ul>
   <li><a href="https://www.universal-robots.com/support/" target="_blank">Universal Robots Support & Download page</a>: Wide range of articles, manuals and SW Downloads.</li>
   <li><a href="https://docs.universal-robots.com/" target="_blank">Universal Robots Documentation</a>: Dedicated URCap, ROS2 and further documentation.</li>
   <li><a href="https://forum.universal-robots.com/" target="_blank">Universal Robots Forum</a>: Community to discuss questions and search existing threads for insights.</li>
   <li><a href="https://discord.com/invite/sEjRgEf6fp" target="_blank">Universal Robots Discord server</a>: Discord server to discuss a broad range of UR Topics.</li>
   <li><a href="https://github.com/UniversalRobots/" target="_blank">Sample code repository</a>: UR Github page.</li>
   <li><a href="https://www.universal-robots.com/marketplace/" target="_blank">UR Marketplace</a>: Showroom displaying all available UR+ products and solutions.</li>
   <li><a href="https://ur.centercode.com/enter/" target="_blank">CenterCode</a>: This is UR's Beta software testing platform where you can access the latest product information and provide feedback on your experience.</li>
   </ul>



Contact Information
^^^^^^^^^^^^^^^^^^^^
For technical consultation, please contact:

| **US:** KRMI@universal-robots.com
| **EMEA:** SKO@universal-robots.com, FLLU@universal-robots.com
| **APAC:** FUNH@universal-robots.com  


When contacting support, please provide:

1. Robot serial number
2. PolyScope version
3. URCap version
4. Description of the issue
5. Error messages (if any)

Frequently Asked Questions
--------------------------

.. admonition:: Q1: How do I check my PolyScope version?

   Go to **Settings** > **System** > **About** to view the PolyScope version.

.. admonition:: Q2: Can I install multiple URCaps?

   Yes, multiple URCaps can be installed simultaneously, provided there are no conflicts.

.. admonition:: Q3: How do I start the UR+ product launch process?

   .. raw:: html

      <p>Please upload your product information to the 
      <a href="https://form.asana.com/?k=9UcMvnNd93yFrOqZQWUKJg&d=66083628180095" target="_blank">UR+ Product Submission Form</a>.
      We will assign a dedicated colleague to work with you on the next steps.</p>

      <p>Please check corresponding content in <a href="product_lifecycle_management.html" target="_blank">Product Life Cycle Management</a>.</p>

.. admonition:: Q4: What Control Box, PolyScope, URCap API and Robot Versions are compatible?

   The table below illustrates the compatibility relationships between Universal Robots' control box,
   software, URCap API versions, and robotic product lines:

   .. image:: images/compatibility_chart.png
      :width: 100%
      :alt: Compatibility Chart

.. admonition:: Q5: What technical skills are required for PolyScope X URCap development?

   Developing URCaps for PolyScope X requires knowledge in the following technology stack:

   .. raw:: html

      <ul>
      <li><a href="https://www.universal-robots.com/manuals/EN/HTML/SW10_11/Content/Landingpages/WebPolyX/LandingScript.htm" target="_blank">URScript</a> - Universal Robots scripting language for robot control, as for this article written date(2026-Jan-16) URScript Directory is the with latest version 10.11.</li>
      <li><strong>RTDE, Rest-API</strong> - Real-Time Data Exchange and REST API for robot communication</li>
      <li><strong>Robotics</strong> - General robotics knowledge and concepts to facilitate the development of the product</li>
      <li><strong>HTML, CSS, TypeScript</strong> - Frontend web technologies for UI development</li>
      <li><a href="https://angular.dev/" target="_blank">Angular</a> - Frontend framework used in PolyScope X, as for this article written date(2026-Jan-16) PolyScope X is adopting Angular 19.</li>
      <li><strong>Docker</strong> - Containerization for development environment and deployment</li>
      </ul>
   
.. admonition:: Q6: How can I quickly get started with PolyScope X URCap programming?

   .. raw:: html

      <p>We offer PolyScope X URCap SDK training (Entry / Advanced) to help developers quickly understand URCap
      functionality and development techniques. Please visit the
      <a href="https://academy.universal-robots.com/our-training-courses/" target="_blank">Universal Robots Academy Training Courses</a>
      page and select "PolyScope X URCap Training" in the Course Type filter to find
      specific course information.</p>

   .. image:: images/urcap_sdk_training_snapshot.png
      :width: 80%
      :alt: PolyScope X URCap SDK Training

   .. raw:: html

      <hr style="margin: 20px 0;">
      <p style="color: red; font-weight: bold;">Entry Agenda [2 day program]:</p>

   1. How to get started and setup your system to run the SDK inside the development container
   2. Start and access the PolyScope X URSim
   3. Create a URCap project
   4. Develop a simple URCap Light-Up following the Getting Started section

   .. image:: images/urcap_sdk_training_basic.png
      :width: 80%
      :alt: PolyScope X URCap SDK Entry Training

   .. raw:: html

      <hr style="margin: 20px 0;">
      <p style="color: red; font-weight: bold;">Advanced Agenda [2 day program]:</p>

   .. image:: images/urcap_sdk_training_advanced.png
      :width: 80%
      :alt: PolyScope X URCap SDK Advanced Training


Reporting Issues
----------------

.. raw:: html

   <a href="https://ur.centercode.com/enter/" target="_blank">To report a bug or issue via CenterCode</a>



.. tip::
   Include screenshots or videos when reporting visual issues.

