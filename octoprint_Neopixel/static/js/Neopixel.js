/*
 * View model for OctoPrint-Neopixel
 *
 * Author: Mickael SEBIRE
 * License: AGPLv3
 */
$(function() {
    function NeopixelViewModel(parameters) {
        var self = this;

		self.settingsViewModel = parameters[0];
		self.light = ko.observable();
		self.onAfterBinding = function() {
			$.ajax({
				url: API_BASEURL + "plugin/neopixel",
				type: "POST",
				dataType: "json",
				data: JSON.stringify({
				command: "light"
			}),
			contentType: "application/json; charset=UTF-8"
		})
		self.btnclass = ko.pureComputed(function() {
			return self.streaming() ? 'btn-danger' : 'btn-primary';
		});
	}

	 self.lightOn = function() {
        $.ajax({
            url: API_BASEURL + "plugin/neopixel",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                     command: "lighton"
            }),
            contentType: "application/json; charset=UTF-8"
        })
    }
	self.lightOff = function() {
		$.ajax({
			url: API_BASEURL + "plugin/neopixel",
			type: "POST",
			dataType: "json",
			data: JSON.stringify({
				command: "lightoff"
			}),
			contentType: "application/json; charset=UTF-8"
		})
	}

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: NeopixelViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ /* "loginStateViewModel", "settingsViewModel" */ ],
        // Elements to bind to, e.g. #settings_plugin_Neopixel, #tab_plugin_Neopixel, ...
        elements: ["#neopixel_navbar_lightOn", "#neopixel_navbar_lightOff"]
    });
});
