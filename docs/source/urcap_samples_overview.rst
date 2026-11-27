Overview - URCap Samples
========================

This page collects URCap sample projects for PolyScope X. Select a card to
open its description.

.. toctree::
   :hidden:

   rtde_monitor
   tool_modbus_driver

.. raw:: html

   <link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;700&amp;display=swap" rel="stylesheet">
   <div class="sample-grid">
   <button type="button" class="sample-card" data-dialog="sample-sdk">
   <span class="sample-card-index">1</span>
   <span class="sample-card-title">SDK samples</span>
   <span class="sample-card-blurb">Samples included with SDK 0.22</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-rtde">
   <span class="sample-card-index">2</span>
   <span class="sample-card-title">RTDE Monitor</span>
   <span class="sample-card-blurb">Registers and controller outputs</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-modbus">
   <span class="sample-card-index">3</span>
   <span class="sample-card-title">Tool Modbus Driver</span>
   <span class="sample-card-blurb">Modbus RTU over tool I/O</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-jog">
   <span class="sample-card-index">4</span>
   <span class="sample-card-title">Step Jogging Tool</span>
   <span class="sample-card-blurb">Step jogging on PolyScope X</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-custom-api">
   <span class="sample-card-index">5</span>
   <span class="sample-card-title">Custom API for PolyScope X</span>
   <span class="sample-card-blurb">Parent and child nodes share values</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-webcam">
   <span class="sample-card-index">6</span>
   <span class="sample-card-title">Simple Webcam</span>
   <span class="sample-card-blurb">USB camera on a physical controller</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-3d">
   <span class="sample-card-index">7</span>
   <span class="sample-card-title">Three Dimension Contribution</span>
   <span class="sample-card-blurb">glTF models in the 3D view</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-tool-io">
   <span class="sample-card-index">8</span>
   <span class="sample-card-title">Accessing Services — Tool Outputs</span>
   <span class="sample-card-blurb">Live Tool I/O signals</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-script">
   <span class="sample-card-index">9</span>
   <span class="sample-card-title">Script Communicator</span>
   <span class="sample-card-blurb">URScript over Primary/Secondary</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-vision">
   <span class="sample-card-index">10</span>
   <span class="sample-card-title">Vision Template</span>
   <span class="sample-card-blurb">Program-node template</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-global">
   <span class="sample-card-index">11</span>
   <span class="sample-card-title">Global Variable</span>
   <span class="sample-card-blurb">A boolean global variable</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-alias">
   <span class="sample-card-index">12</span>
   <span class="sample-card-title">Signal Alias</span>
   <span class="sample-card-blurb">Output aliases in a dropdown</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-daemon">
   <span class="sample-card-index">13</span>
   <span class="sample-card-title">Dual Daemon</span>
   <span class="sample-card-blurb">Two daemon containers</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-ellipse">
   <span class="sample-card-index">14</span>
   <span class="sample-card-title">Ellipse Path</span>
   <span class="sample-card-blurb">MoveL waypoints on an ellipse</span>
   </button>
   <button type="button" class="sample-card" data-dialog="sample-serial">
   <span class="sample-card-index">15</span>
   <span class="sample-card-title">Serial Hotplug</span>
   <span class="sample-card-blurb">Modbus RTU on USB-RS485</span>
   </button>
   </div>

   <div class="sample-modal" hidden>
   <div class="sample-modal-backdrop" data-close></div>
   <div class="sample-modal-panel" role="dialog" aria-modal="true" aria-labelledby="sample-modal-title">
   <button type="button" class="sample-modal-close" data-close aria-label="Close">&times;</button>
   <h2 id="sample-modal-title" class="sample-modal-title"></h2>
   <div class="sample-modal-body"></div>
   </div>
   </div>

.. container:: sample-detail
   :name: sample-sdk

   The samples are folders under ``samples/`` in the SDK workspace, beside
   ``newurcap.sh``. SDK 0.22 is the SDK released with PolyScope X 10.15. Every
   sample below is included in that SDK.

   .. raw:: html

      <p>Descriptions follow the
      <a href="https://docs.universal-robots.com/PolyScopeX_SDK_Documentation/build/SDK-v0.22/UserGuide.html" target="_blank">SDK User Guide</a>.
      The release note is in the
      <a href="https://docs.universal-robots.com/PolyScopeX_SDK_Documentation/build/SDK-v0.22/Changelog.html" target="_blank">SDK 0.22 changelog</a>:
      SDK 0.22.142 is compatible with PolyScope X 10.15.</p>

      <div class="sdk-sample-scroll">
      <table class="sdk-sample-table">
      <thead>
      <tr>
      <th>Sample</th>
      <th>Location</th>
      <th>Function</th>
      <th>SDK</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td>calibration-info</td>
      <td><code>samples/calibration-info</code></td>
      <td>Reads calibration information from the controller in a Docker container contribution.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>datastorage</td>
      <td><code>samples/datastorage</code></td>
      <td>Shows ways to store data in a Docker container contribution.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>devices</td>
      <td><code>samples/devices</code></td>
      <td>Communicates with a serial device from a Docker container contribution.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>global-variables-sidebar-item</td>
      <td><code>samples/global-variables-sidebar-item</code></td>
      <td>Lists global variables in a sidebar contribution while a program is running.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>gripdistance</td>
      <td><code>samples/gripdistance</code></td>
      <td>Application contribution that configures the grip distance of a gripper.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>macvlan</td>
      <td><code>samples/macvlan</code></td>
      <td>Sets up a virtual network interface in a Docker container contribution.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>rtde-sample</td>
      <td><code>samples/rtde-sample</code></td>
      <td>Talks to the controller RTDE interface from a Docker container contribution.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-docker</td>
      <td><code>samples/simple-docker</code></td>
      <td>Docker container contribution and an application contribution that communicates with it.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-gripper</td>
      <td><code>samples/simple-gripper</code></td>
      <td>Full gripper contribution using ROS 2 and the tool serial interface.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-operator-screen</td>
      <td><code>samples/simple-operator-screen</code></td>
      <td>Operator Screen selected from the Application menu “Operator Screen”.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-rest</td>
      <td><code>samples/simple-rest</code></td>
      <td>REST communication between the Docker backend and the web frontend.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-ros2-node</td>
      <td><code>samples/simple-ros2-node</code></td>
      <td>ROS 2 node in a Docker container that talks to the controller with urinterfaces messages in Python.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-websocket</td>
      <td><code>samples/simple-websocket</code></td>
      <td>WebSocket communication between the Docker backend and the web frontend.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>simple-xmlrpc</td>
      <td><code>samples/simple-xmlrpc</code></td>
      <td>URScript and the frontend both talk to a backend over XML-RPC.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>smart-skill-teach-mode</td>
      <td><code>samples/smart-skill-teach-mode</code></td>
      <td>Smart Skill that uses Teach Mode.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>ur-program-nodes</td>
      <td><code>samples/ur-program-nodes</code></td>
      <td>The program nodes shipped with PolyScope X: assignment, loop, move-to, set, tool-force, and wait.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>usb-hotplug</td>
      <td><code>samples/usb-hotplug</code></td>
      <td>Accesses hot-plug devices from a URCap through the container hot-plug mechanism.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      <tr>
      <td>xmlrpc-gripper</td>
      <td><code>samples/xmlrpc-gripper</code></td>
      <td>Full gripper contribution using XML-RPC and the tool serial interface.</td>
      <td>0.22<br>PolyScope X 10.15</td>
      </tr>
      </tbody>
      </table>
      </div>

.. container:: sample-detail
   :name: sample-rtde

   RTDE Monitor shows RTDE general-purpose registers and the other controller
   outputs on one Operator Screen. The full article is :doc:`rtde_monitor`.

   .. image:: images/rtde_monitor_2.png
      :width: 100%
      :alt: RTDE Monitor with the Register page selected

.. container:: sample-detail
   :name: sample-modbus

   Tool Modbus Driver is a URCapX for customized Modbus RTU communication over
   tool I/O. The full article is :doc:`tool_modbus_driver`.

   .. image:: images/tool_modbus_3_application_overview.png
      :width: 100%
      :alt: Tool Modbus Driver application overview

.. container:: sample-detail
   :name: sample-jog

   .. raw:: html

      <p>A PolyScope X URCap for step jogging. The forum post includes the URCapX
      download:
      <a href="https://forum.universal-robots.com/t/step-jogging-tool-urcap/41857/6" target="_blank">Step Jogging Tool URCap</a>.</p>

   .. image:: images/sample_step_jogging.jpeg
      :width: 100%
      :alt: Step Jog Tool with plus and minus buttons for X, Y, Z, RX, RY, and RZ

.. container:: sample-detail
   :name: sample-custom-api

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/custom-api-polyscopex" target="_blank">custom-api-polyscopex</a>
      inserts a child program node from a parent node and lets the parent change a
      value on the child. The child can also change a value on the parent.</p>

.. container:: sample-detail
   :name: sample-webcam

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/simple-webcam" target="_blank">simple-webcam</a>
      accepts a USB webcam on a physical controller and shows the feed in the
      frontend, with a toggle and a snapshot. It does not run on the simulator.</p>

.. container:: sample-detail
   :name: sample-3d

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/three-dimension-contribution-x" target="_blank">three-dimension-contribution-x</a>
      is a sidebar URCap that adds and removes glTF models in the PolyScope X 3D
      view, including a gripper on the tool flange.</p>

   .. image:: images/sample_three_dimension.png
      :width: 100%
      :alt: Sidebar toggles for a Robotiq 2F-85 and a duck in the 3D view

.. container:: sample-detail
   :name: sample-tool-io

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/accessing_services_tool_outputs" target="_blank">accessing_services_tool_outputs</a>
      reads Universal Robots Tool I/O signals and shows them in a web
      contribution.</p>

   .. image:: images/sample_tool_outputs.png
      :width: 100%
      :alt: Tool I/O analog and digital signals in the Access Services application

.. container:: sample-detail
   :name: sample-script

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/script-communicator-x" target="_blank">script-communicator-x</a>
      sends URScript to the controller over the Primary/Secondary interface and
      reads values back from the running script, such as a popup and the current
      TCP pose.</p>

   .. image:: images/sample_script_communicator.png
      :width: 100%
      :alt: Script Communicator application showing the actual TCP pose

.. container:: sample-detail
   :name: sample-vision

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/vision-template-x" target="_blank">vision-template-x</a>
      is an Angular URCap template for program nodes: insert a child node,
      customize a motion profile, customize a classic joint node, use a folder
      with a child, and set a node icon.</p>

   .. image:: images/sample_vision_template.png
      :width: 100%
      :alt: Vision template program node with inserted child nodes

.. container:: sample-detail
   :name: sample-global

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/global-variable-x" target="_blank">global-variable-x</a>
      creates a boolean global variable with the <code>VariableDeclaration</code>
      interface and writes it into the program as <code>global var=False</code>.</p>

.. container:: sample-detail
   :name: sample-alias

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/Signal-Alias-x" target="_blank">Signal-Alias-x</a>
      lists Digital Outputs and Configurable Outputs and shows the alias configured
      for each signal.</p>

   .. image:: images/sample_signal_alias.png
      :width: 100%
      :alt: Digital Output dropdown showing configured signal aliases

.. container:: sample-detail
   :name: sample-daemon

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/my_daemon_dual_polyscopex" target="_blank">my_daemon_dual_polyscopex</a>
      packages two daemon containers in one URCap. Each container has its own
      ingress.</p>

.. container:: sample-detail
   :name: sample-ellipse

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/ellipse-polyscope-x" target="_blank">ellipse-polyscope-x</a>
      is a program node. After the center pose is set, it inserts blended MoveL
      waypoints that trace an ellipse around that center.</p>

.. container:: sample-detail
   :name: sample-serial

   .. raw:: html

      <p><a href="https://github.com/FuNingHu/serial-hotplug-PolyScopeX" target="_blank">serial-hotplug-PolyScopeX</a>
      finds a hot-plugged USB-RS485 port and talks Modbus RTU to a gripper: scan
      the slave address, enable it, and command position, speed, and torque.</p>
