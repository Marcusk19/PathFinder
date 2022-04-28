PathFinder
==========
These are the underlying modules for the PathFinder. Each one has a specific role to perform and most are tied together under
our two large "main" modules: OBD.py and HUD.py. A python file main.py is used as an entrypoint for the program and each main
module takes their own respective thread to run concurrently.

.. code-block:: python

   # an instance of OBD and HUD declared and ran
   def main():
      screen = display.Display()
      obd = OBD.Obd(screen)
      hud = HUD.Hud(screen)
      hud.start()
      obd.start()

.. toctree::
   :maxdepth: 4

   pathfinder

MQTT
====
One more important thing to note is that the PathFinder relies on a connection to a MQTT broker. For development 
the Eclipse Mosquitto docker image was used as the backing broker for our communications. A simple web-app built
with the flask framework was then written to facilitate users sending information to our Raspberry Pi. 
If you want to see the underlying code for the web-app, you can check it out at `<https://github.com/Marcusk19/MQTT-web-app>`_