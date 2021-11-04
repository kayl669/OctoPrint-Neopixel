# coding=utf-8
from __future__ import absolute_import

import os
import octoprint.plugin
from octoprint.server import user_permission

class NeopixelPlugin(octoprint.plugin.StartupPlugin,
                     octoprint.plugin.SimpleApiPlugin,
                     octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.AssetPlugin):

        def on_after_startup(self):
               self._logger.info("==============================================================================================")
               self._logger.info("NeoPixel loaded!!!")
               self._logger.info("==============================================================================================")

        def get_api_commands(self):
               return dict(
                      lighton=[],
                      lightoff=[]
                      )

        def on_api_command(self, command, data):
               if command == "lighton":
                    self._logger.info("light on called")
                    os.system("sudo ./lighton")
                    return
               elif command == "lightoff":
                    self._logger.info("light off called")
                    os.system("sudo ./lightoff")
                    return

        def on_api_get(self, request):
               return flask.jsonify(foo="bar")

        ##~~ AssetPlugin

        def get_assets(self):
                return dict(
                    js=["js/Neopixel.js"]
                )


        def get_update_information(self):
            # Define the configuration for your plugin to use with the Software Update
            # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
            # for details.
            return {
                "Neopixel": {
                    "displayName": "Neopixel Plugin",
                    "displayVersion": self._plugin_version,

                    # version check: github repository
                    "type": "github_release",
                    "user": "kayl669",
                    "repo": "OctoPrint-Neopixel",
                    "current": self._plugin_version,

                    # update method: pip
                    "pip": "https://github.com/kayl669/OctoPrint-Neopixel/archive/{target_version}.zip",
                }
            }


__plugin_name__ = "Neopixel Plugin"
# Starting with OctoPrint 1.4.0 OctoPrint will also support to run under Python 3 in addition to the deprecated
# Python 2. New plugins should make sure to run under both versions for now. Uncomment one of the following
# compatibility flags according to what Python versions your plugin supports!
#__plugin_pythoncompat__ = ">=2.7,<3" # only python 2
__plugin_pythoncompat__ = ">=3,<4" # only python 3
#__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = NeopixelPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
