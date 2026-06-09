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

.. image:: images/codespace.png
   :class: hidden-image

.. image:: images/urcap_sdk_training_snapshot.png
   :class: hidden-image

.. image:: images/urcap_sdk_training_basic.png
   :class: hidden-image

.. image:: images/urcap_sdk_training_advanced.png
   :class: hidden-image

.. image:: images/compatibility_chart.png
   :class: hidden-image

.. raw:: html

   <style>
   .hidden-image {
     display: none;
   }
   .faq-container {
     margin: 20px 0;
   }
   .faq-item {
     margin-bottom: 10px;
     border: 1px solid #6ab0de;
     border-radius: 5px;
     overflow: hidden;
   }
   .faq-question {
     background: #6ab0de;
     color: white;
     padding: 15px;
     cursor: pointer;
     font-weight: bold;
     display: flex;
     justify-content: space-between;
     align-items: center;
     transition: background 0.3s;
   }
   .faq-question:hover {
     background: #5a9fcd;
   }
   .faq-icon {
     font-size: 20px;
     transition: transform 0.3s;
     color: white;
   }
   .faq-icon.open {
     transform: rotate(180deg);
   }
   .faq-answer {
     max-height: 0;
     overflow: hidden;
     transition: max-height 0.3s ease-out;
     padding: 0 15px;
     background: #e7f2fa;
   }
   .faq-answer.open {
     max-height: 5000px;
     padding: 15px;
     transition: max-height 0.5s ease-in;
   }
   .faq-answer p {
     margin: 10px 0;
   }
   .faq-answer img {
     max-width: 80%;
     height: auto;
     margin: 15px 0;
   }
   .faq-answer ul {
     margin: 10px 0;
     padding-left: 20px;
   }
   .faq-answer li {
     margin: 5px 0;
   }
   </style>

   <div class="faq-container">
     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q1: How do I check my PolyScope version?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>Go to <strong>Settings</strong> &gt; <strong>System</strong> &gt; <strong>About</strong> to view the PolyScope version.</p>
       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q2: Can I install multiple URCaps?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>Yes, multiple URCaps can be installed simultaneously, provided there are no conflicts.</p>
       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q3: How do I start the UR+ product launch process?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>Please upload your product information to the 
         <a href="https://form.asana.com/?k=9UcMvnNd93yFrOqZQWUKJg&d=66083628180095" target="_blank">UR+ Product Submission Form</a>.
         We will assign a dedicated colleague to work with you on the next steps.</p>
         <p>Please check corresponding content in <a href="product_lifecycle_management.html" target="_blank">Product Life Cycle Management</a>.</p>
       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q4: What Control Box, PolyScope, URCap API and Robot Versions are compatible?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>The table below illustrates the compatibility relationships between Universal Robots' control box,
         software, URCap API versions, and robotic product lines:</p>
         <img src="_images/compatibility_chart.png" alt="Compatibility Chart" style="width: 100%;">
       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q5: What technical skills are required for PolyScope X URCap development?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>Developing URCaps for PolyScope X requires knowledge in the following technology stack:</p>
         <ul>
           <li><a href="https://www.universal-robots.com/manuals/EN/HTML/SW10_11/Content/Landingpages/WebPolyX/LandingScript.htm" target="_blank">URScript</a> - Universal Robots scripting language for robot control, as for this article written date(2026-Jan-16) URScript Directory is the with latest version 10.11.</li>
           <li><strong>RTDE, Rest-API</strong> - Real-Time Data Exchange and REST API for robot communication</li>
           <li><strong>Robotics</strong> - General robotics knowledge and concepts to facilitate the development of the product</li>
           <li><strong>HTML, CSS, TypeScript</strong> - Frontend web technologies for UI development</li>
           <li><a href="https://angular.dev/" target="_blank">Angular</a> - Frontend framework used in PolyScope X, as for this article written date(2026-Jan-16) PolyScope X is adopting Angular 19.</li>
           <li><strong>Docker</strong> - Containerization for development environment and deployment</li>
         </ul>
       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q6: How can I quickly get started with PolyScope X URCap programming?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>We offer PolyScope X URCap SDK training (Entry / Advanced) to help developers quickly understand URCap
         functionality and development techniques. Please visit the
         <a href="https://academy.universal-robots.com/our-training-courses/" target="_blank">Universal Robots Academy Training Courses</a>
         page and select "PolyScope X URCap Training" in the Course Type filter to find
         specific course information.</p>
         <img src="_images/urcap_sdk_training_snapshot.png" alt="PolyScope X URCap SDK Training" style="width: 80%;">

         <hr style="margin: 30px 0;">
         <p style="color: #c0392b; font-weight: bold; font-size: 1.2em; margin-bottom: 15px;">Entry Agenda [2 day program]:</p>

         <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">

           <div style="flex: 1; min-width: 220px; background: #f8f9fa; border-left: 4px solid #3498db; border-radius: 6px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
             <div style="font-size: 0.8em; color: #3498db; font-weight: bold; margin-bottom: 5px;">MODULE 1</div>
             <div style="font-weight: bold; color: #2c3e50;">Environment Setup</div>
             <p style="font-size: 0.9em; color: #555; margin-top: 8px;">How to get started and setup your system to run the SDK inside the development container</p>
           </div>

           <div style="flex: 1; min-width: 220px; background: #f8f9fa; border-left: 4px solid #2ecc71; border-radius: 6px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
             <div style="font-size: 0.8em; color: #2ecc71; font-weight: bold; margin-bottom: 5px;">MODULE 2</div>
             <div style="font-weight: bold; color: #2c3e50;">URSim Simulator</div>
             <p style="font-size: 0.9em; color: #555; margin-top: 8px;">Start and access the PolyScope X URSim</p>
           </div>

           <div style="flex: 1; min-width: 220px; background: #f8f9fa; border-left: 4px solid #e67e22; border-radius: 6px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
             <div style="font-size: 0.8em; color: #e67e22; font-weight: bold; margin-bottom: 5px;">MODULE 3</div>
             <div style="font-weight: bold; color: #2c3e50;">Create Project</div>
             <p style="font-size: 0.9em; color: #555; margin-top: 8px;">Create a URCap project</p>
           </div>

           <div style="flex: 1; min-width: 220px; background: #f8f9fa; border-left: 4px solid #9b59b6; border-radius: 6px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
             <div style="font-size: 0.8em; color: #9b59b6; font-weight: bold; margin-bottom: 5px;">MODULE 4</div>
             <div style="font-weight: bold; color: #2c3e50;">Light-Up URCap</div>
             <p style="font-size: 0.9em; color: #555; margin-top: 8px;">Develop a simple URCap Light-Up following the Getting Started section</p>
           </div>

         </div>

         <img src="_images/urcap_sdk_training_basic.png" alt="PolyScope X URCap SDK Entry Training" style="width: 80%;">

         <hr style="margin: 30px 0;">
         <p style="color: #c0392b; font-weight: bold; font-size: 1.2em; margin-bottom: 15px;">Advanced Agenda [2 day program]:</p>

         <div style="overflow-x: auto; padding-bottom: 10px;">
         <div style="display: flex; gap: 15px; min-width: max-content; margin-bottom: 20px;">

           <div style="width: 250px; flex-shrink: 0; background: #f0f4f7; border-top: 4px solid #2c3e50; border-radius: 6px; padding: 15px;">
             <div style="font-size: 0.8em; color: #2c3e50; font-weight: bold; margin-bottom: 10px;">MODULE 1 — General</div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Application Sample</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Template for sharing ideas / projects of the community</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Debugging</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">A quick insight in the debugging options available</p>
             </div>
           </div>

           <div style="width: 250px; flex-shrink: 0; background: #f0f4f7; border-top: 4px solid #16a085; border-radius: 6px; padding: 15px;">
             <div style="font-size: 0.8em; color: #16a085; font-weight: bold; margin-bottom: 10px;">MODULE 2 — Application</div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Add Container (XMLRPC)</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Add container and communicate with it via XMLRPC from different points of entry: Behavior Worker / Component / URScript.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); position: relative;">
               <span style="position: absolute; top: 6px; right: 8px; color: #f1c40f; font-size: 1.2em;">&#9733;</span>
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Connection between Application & Program</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Description on how to use the data provided via the application node to configure relevant parts in the correspondent program node.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); position: relative;">
               <span style="position: absolute; top: 6px; right: 8px; color: #f1c40f; font-size: 1.2em;">&#9733;</span>
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">How to show external Web content</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">The web based foundation of PolyScope X allows for simple ways to add existing Web content.</p>
             </div>
           </div>

           <div style="width: 250px; flex-shrink: 0; background: #f0f4f7; border-top: 4px solid #2980b9; border-radius: 6px; padding: 15px;">
             <div style="font-size: 0.8em; color: #2980b9; font-weight: bold; margin-bottom: 10px;">MODULE 3 — Program</div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Expand on multiple UI-Elements</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Learn how to utilize different UI Elements and how to implement them.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); position: relative;">
               <span style="position: absolute; top: 6px; right: 8px; color: #f1c40f; font-size: 1.2em;">&#9733;</span>
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Create additional dialog window</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">To allow for further customization a separate dialog window can be opened through a program node.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Access application / robot information</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Introduce in how to access robot / application data via the typescript API. This covers reading out the robot type to how to define a custom TCP.</p>
             </div>
           </div>

           <div style="width: 250px; flex-shrink: 0; background: #f0f4f7; border-top: 4px solid #d35400; border-radius: 6px; padding: 15px;">
             <div style="font-size: 0.8em; color: #d35400; font-weight: bold; margin-bottom: 10px;">MODULE 4 — Container</div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">General Setup</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Introduction on how to setup a container, what files to add and adjust.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Communication with external devices</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">What options are available to setup a communication channel from the container to an external device.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">ROS2 – Webbridge / Messaging Bus</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Introduction in how to use the ROS2 – Webbridge as a way to gather robot data.</p>
             </div>
           </div>

           <div style="width: 250px; flex-shrink: 0; background: #f0f4f7; border-top: 4px solid #8e44ad; border-radius: 6px; padding: 15px;">
             <div style="font-size: 0.8em; color: #8e44ad; font-weight: bold; margin-bottom: 10px;">MODULE 5 — Optional</div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Smart Skills</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Get an overview on how to create a basic Smart Skill. It also covers how to add parametrization from the application part.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); position: relative;">
               <span style="position: absolute; top: 6px; right: 8px; color: #f1c40f; font-size: 1.2em;">&#9733;</span>
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Supporting multiple languages</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Brief insight in how to setup your URCap to easily add more languages for the UI.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Program Node Configuration</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Ways to adjust program nodes and their options in the program tree.</p>
             </div>
             <div style="background: white; border-radius: 5px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
               <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">Overview of HTML & CSS Layout</div>
               <p style="font-size: 0.85em; color: #555; margin-top: 6px; margin-bottom: 0;">Insight in different ways to adjust the design and layout of your HTML site.</p>
             </div>
           </div>

         </div>
         </div>

       </div>
     </div>

     <div class="faq-item">
       <div class="faq-question" onclick="toggleFaq(this)">
         <span>Q7: How to quickly open PolyScope X simulator?</span>
         <span class="faq-icon">▼</span>
       </div>
       <div class="faq-answer">
         <p>On the official Universal Robots GitHub, we provide a <a href="https://github.com/UniversalRobots/PolyScopeX_URCap_SDK" target="_blank">Codespace-based SDK</a> that requires no local installation. You can open the SDK environment and run URSim there.</p>
         <p style="text-align: center; margin: 20px 0;">
           <a href="https://github.com/UniversalRobots/PolyScopeX_URCap_SDK" target="_blank">
             <img src="_images/codespace.png" alt="PolyScope X Codespace SDK" style="width: 80%; cursor: pointer; border: 2px solid #6ab0de; border-radius: 5px;">
           </a>
         </p>
         <p>Generally, Codespace offers a free usage quota that is sufficient for regular users, making this the fastest way to access the PolyScope X software.</p>
         <p><strong>What you need to prepare:</strong></p>
         <ol>
           <li>A GitHub account</li>
           <li>A stable and fast internet connection</li>
         </ol>
         <p><strong>Important Note:</strong> The simulator running here has minor differences in protocol compared to the real robot. We will explain these differences in detail during the Entry/Advanced SDK training.</p>
       </div>
     </div>
   </div>

   <script>
   function toggleFaq(element) {
     var answer = element.nextElementSibling;
     var icon = element.querySelector('.faq-icon');
     
     // Close all other FAQs
     var allAnswers = document.querySelectorAll('.faq-answer');
     var allIcons = document.querySelectorAll('.faq-icon');
     
     allAnswers.forEach(function(item) {
       if (item !== answer) {
         item.classList.remove('open');
       }
     });
     
     allIcons.forEach(function(item) {
       if (item !== icon) {
         item.classList.remove('open');
       }
     });
     
     // Toggle current FAQ
     answer.classList.toggle('open');
     icon.classList.toggle('open');
   }
   </script>


Reporting Issues
----------------

.. raw:: html

   <a href="https://ur.centercode.com/enter/" target="_blank">To report a bug or issue via CenterCode</a>



.. tip::
   Include screenshots or videos when reporting visual issues.

