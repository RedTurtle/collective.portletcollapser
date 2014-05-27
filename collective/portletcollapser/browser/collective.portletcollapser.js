/**
 *
 * ExpandCollapse jQuery plugin
 *
 * Version 0.1 (03-05-2014)
 * RedTurtle Technology
 *
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 * @author Andrea Cecchi (cekk)
 */
/*jslint browser: true*/
/*global jQuery */

(function ($) {
    "use strict";
    function save_data(key, value) {
        if ((window.sessionStorage !== "undefined") && window.sessionStorage !== null) {
            sessionStorage.setItem(key, value);
        }
    }
    function read_data(key) {
        if ((window.sessionStorage !== "undefined") && window.sessionStorage !== null) {
            return sessionStorage.getItem(key);
        }
    }
    var methods = {
        init : function (options) {
            // # Set base settings
            var defaults = {
                default_state: "expanded",
                speed: "slow"
            };
            // # Use $.extend function to merge default settings with given settings
            options = $.extend(defaults, options);
            $(this).addClass('collapsiblePortlet');
            var wrapper_id = $(this).parents('div.portletWrapper').attr('id'),
                portlet_header = $(this).find('dt');
            if (read_data(wrapper_id) === null) {
                if ((options.default_state === "collapsed")) {
                    methods.collapse.apply(portlet_header);
                } else {
                    methods.expand.apply(portlet_header);
                }
            } else {
                if ((read_data(wrapper_id) === "collapsed")) {
                    methods.collapse.apply(portlet_header);
                } else {
                    methods.expand.apply(portlet_header);
                }
            }
        },
        expand : function () {
            var wrapper = $(this).parents('div.portletWrapper'),
                parent = $(this).parent();
            wrapper.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideDown();
                }
            });
            if (parent.hasClass('portletCollapsed')) {
                parent.removeClass("portletCollapsed");
            }
            if (!parent.hasClass('portletExpanded')) {
                parent.addClass("portletExpanded");
            }
            save_data(wrapper.attr('id'), 'expanded');
            return this;
        },
        collapse : function () {
            var wrapper = $(this).parents('div.portletWrapper'),
                parent = $(this).parent();
            wrapper.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideUp();
                }
            });

            if (parent.hasClass('portletExpanded')) {
                parent.removeClass("portletExpanded");
            }
            if (!parent.hasClass('portletCollapsed')) {
                parent.addClass("portletCollapsed");
            }
            save_data(wrapper.attr('id'), "collapsed");
            return this;
        },
        toggle : function () {
            var wrapper = $(this).parents('div.portletWrapper'),
                parent = $(this).parent(),
                wrapper_id = wrapper.attr('id');
            wrapper.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideToggle();
                }
            });
            parent.toggleClass("portletCollapsed").toggleClass("portletExpanded");
            if (read_data(wrapper_id) === "expanded") {
                save_data(wrapper_id, "collapsed");
            } else {
                save_data(wrapper_id, "expanded");
            }
            return this;
        }
    };

    $.fn.collapsePortlet = function (method) {
        // Method calling logic
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        }
        if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        }
        //if methods are invalid, set and error.
        $.error('Method ' +  method + ' does not exist on jQuery.collapsePortlet');
    };
}(jQuery));
