from pytube import YouTube
import os

def load_plugin(plugin, plugin_type):
  if plugin_type == 'start':
    print("First check: Good")
  else:
    if plugin_type =='end':
      print("Second check: Good")
    else:
      print("Error: Unknown plugin type " + plugin_type)
      print("Error code: 1021")
      print("Please change to a corret plugin type!")
      exit()
  print("Loading plugin...")
  print("Loading plugin type... " + str(plugin_type))
  os.system("python3 Plugins/" + str(plugin) + str("/main.py"))

load_plugin("Skip_Plugin", "start")