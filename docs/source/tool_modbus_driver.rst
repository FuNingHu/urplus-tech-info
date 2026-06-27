[Debugging Tool] Tool Modbus Driver
====================================

This project offers a URCapX tooling that facilitates customized Modbus RTU
communication over tool-IO.

Dependencies
------------

PolyScope X 10.13+.

----

Using the ApplicationNode
-------------------------

The ``ApplicationNode`` is the persisted configuration object for this app node.
Its interface is defined in
``tool-modbus-driver-frontend/src/app/components/tool-modbus-driver-app/tool-modbus-driver-app.node.ts``.

.. image:: images/tool_modbus_3_application_overview.png
   :alt: Application overview
   :width: 60%

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - ``deviceAddress``
     - Modbus slave address (1–254)
   * - ``baudrate``
     - Baud rate, e.g. ``9600``
   * - ``verification``
     - Serial verification: ``None 8 1`` / ``Odd 8 1`` / ``Even 8 1`` (parity / bytesize / stopbits)
   * - ``isSimulation``
     - Real / Simulation toggle
   * - ``isConnect``
     - Whether connected (mirrors the Connect/Disconnect button state)
   * - ``monitorSignals``
     - List of monitored signals; each has ``mode`` (Read/Write), ``name``, ``register``, ``frequency``, ``writeValue``, ``autoIncrement``

Monitoring registers (Monitor)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click **Connect** to open the connection, then use the **Monitor (R/W register)**
card to watch and drive registers live:

- Press **+** to add a signal row; press **−** to remove one.
- Set each row's **Mode** (Read/Write), **Name**, **Register**, and **Frequency** (Hz).
- In **Read** mode the polled value is shown in the **Value** field.
- In **Write** mode type a value to send; enable **auto increment by 1** to increment and
  write it every ``1/Frequency`` seconds.

.. image:: images/tool_modbus_2_application_online_monitor.png
   :alt: Online register monitor
   :width: 60%

Scanning for the device address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not know the device's slave address, click **Scan**. It probes
addresses from 1 and stops at the first device that responds, showing the found
Device Address on the button and in a success notification. Set the matching
**Baudrate** / **Verification** before scanning so the device can answer.

.. image:: images/tool_modbus_1_scan_found.png
   :alt: Scan found a device
   :width: 60%

----

Working with pre-defined URScript functions in Robot Program
------------------------------------------------------------

Once this app node is added to a program, URCapX automatically injects the
script functions below in the preamble (in the **Before Start** section, defined
in ``tool-modbus-driver-app.behavior.worker.ts``). They can be called directly
from Script nodes / expressions:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Pre-defined functions
     - Purpose
   * - ``tool_modbus_read(register_address_start, count=1, slave_id=<deviceAddress>)``
     - Read registers; returns a list of ``count`` values
   * - ``tool_modbus_write(register_address_start, data, count=1, slave_id=<deviceAddress>)``
     - Write registers; ``data`` is a single value or comma-separated values
   * - ``tool_modbus_open(com, bau, my_id)``
     - Power on the tool and open the Modbus master
   * - ``close_modbus_master()``
     - Close the Modbus master
   * - ``is_tool_modbus_service_reachable()``
     - Whether the backend service is reachable
   * - ``is_tool_modbus_connected()``
     - Whether currently connected
   * - ``get_modbus_error_info()``
     - Read error information
   * - ``get_modbus_my_id()``
     - Read the current slave address

Examples:

.. code-block:: urscript

   # 1. Check the service reachable
   if is_tool_modbus_service_reachable():

       # 2. Open the Modbus master
       tool_modbus_open("/dev/ur-ttylink/ttyTool", "9600", 10, "None 8 1")

       # 3a. Read 2 values from registers 100, 101; 
       # the return value is a list of 2 values, i.e., [value1, value2].
       values = tool_modbus_read(100, count=2)
       temperature = values[0] #retrive the first value..
       humidity = values[1]
       
       # 3b. Read 1 value from register 100
       value = tool_modbus_read(100)

       # 4a. Write an array of 3 values to registers 100, 101, 102
       tool_modbus_write(100, [1, 2, 3], count=3)

       # 4b. Or write 5 to register 100
       tool_modbus_write(100, 5)
   end

For safer read/write, guard the calls with ``is_tool_modbus_connected()`` so
they only run once the connection is actually established:

.. code-block:: urscript

   # Only read/write when the Modbus connection is established
   if is_tool_modbus_connected():

       # Read 1 value from register 100
       value = tool_modbus_read(100)

       # Write an array of 3 values to registers 100, 101, 102
       tool_modbus_write(100, [1, 2, 3], count=3)
   end

Talking to multiple devices on the same bus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``tool_modbus_read`` / ``tool_modbus_write`` accept an optional **``slave_id``**
as the last argument so you can address several slaves that share the same tool
serial bus **without re-opening the master** for each one. The driver serializes
bus access internally, so calls to different slaves are safe back-to-back.

- The ``slave_id`` default is the **device address configured on the app page**
  (``deviceAddress``), baked into the preamble when the program is generated.
  Omitting it therefore targets the configured device, keeping existing programs
  backward compatible.
- Pass a non-zero ``slave_id`` to talk to a specific slave; pass ``0`` (or omit
  it) to use the configured device address.
- ``slave_id`` is the **last** positional argument. URScript can only drop
  trailing defaults, so to set ``slave_id`` you must also pass ``count``, e.g.
  ``tool_modbus_read(100, 1, 11)``.

.. code-block:: urscript

   if is_tool_modbus_connected():

       # Read register 100 from slave 10 (the configured device in Application Node)
       value_10 = tool_modbus_read(100, 1)

       # Read register 100 from slave 11 on the same bus (no re-open needed)
       value_11 = tool_modbus_read(100, 1, 11)

       # Write 5 to register 100 of slave 12
       tool_modbus_write(100, 5, 1, 12)
   end

Alternatively, you may open the master for each slave address in turn,
read/write, then close before switching to the next one:

.. code-block:: urscript

   tool_modbus_open("/dev/ur-ttylink/ttyTool", "9600", 10, "None 8 1")
   # open the Modbus master for slave address 10, baudrate 9600, verification (Parity None, Bytesize 8, Stopbits 1).
   value = tool_modbus_read(100)  # read the value from register 100.
   sleep(0.1)
   close_modbus_master()  # close the Modbus master.

   tool_modbus_open("/dev/ur-ttylink/ttyTool", "9600", 11, "None 8 1")
   # open the Modbus master for slave address 11.
   value = tool_modbus_read(100)
   sleep(0.1)
   close_modbus_master()
   # so on and so forth...

.. admonition:: Notes
   :class: tip

   - Register reads/writes use the connection opened by ``tool_modbus_open`` in the
     preamble (which applies the node's baud rate / address / verification).
   - In **Simulation** mode the serial port is not actually opened, so script
     calls do not communicate with hardware.

----

Disabling the Tool or Using a Custom Communication Setup
--------------------------------------------------------

Disabling the tool
^^^^^^^^^^^^^^^^^^^

When you do not need the Tool Modbus feature, select **Simulation** on the
application page. This turns the feature off without affecting the robot runtime
(the tool serial port is not opened).

.. image:: images/tool_modbus_4_simulation_toggler.png
   :alt: Simulation toggle
   :width: 50%


Further help
------------

Get more help by contacting ( funh@universal-robots.com )

----

.. admonition:: Download
   :class: note

   .. raw:: html

      <p>URCapX download:
      <a href="https://github.com/FuNingHu/tool-modbus-driver-x/tree/main/target" target="_blank">LINK</a></p>

   .. image:: images/tool_modbus_5_download_urcapx.png
      :alt: Download the URCapX package
      :width: 20%

----

License
-------

Released under the **MIT License**. The software is
provided "as is", without warranty of any kind. You are free to use, copy,
modify, and distribute it, provided the original copyright and license notice
are retained.

.. raw:: html

   <p>See the full license text:
   <a href="https://github.com/FuNingHu/tool-modbus-driver-x/blob/main/LICENSE" target="_blank">LICENSE</a></p>
