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

    // function cookie_value() {
    //     var c_value = document.cookie, c_start = c_value.indexOf(" expandcollapse=");
    //     if (c_start === -1) {
    //         c_start = c_value.indexOf("expandcollapse=");
    //     }
    //     if (c_start === -1) {
    //         c_value = null;
    //     } else {
    //         var c_start = c_value.indexOf("=", c_start) + 1, c_end = c_value.indexOf(";", c_start);
    //         if (c_end === -1) {
    //            c_end = c_value.length;
    //         }
    //         c_value = unescape(c_value.substring(c_start,c_end));
    //     }
    //     return c_value;
    // }

    function save_data(key, value) {
        if ((window.sessionStorage !== "undefined") && window.sessionStorage !== null) {
            sessionStorage.setItem(key, value);
        }
    }

    function read_data(key) {
        if ((window.sessionStorage !== "undefined") && window.sessionStorage !== null) {
            return sessionStorage.getItem(key);
        }
        // return cookie_value();
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
            var wrapper_id = $(this).parents('div.portletWrapper').attr('id');
            if (read_data(wrapper_id) === null) {
                if ((options.default_state === "collapsed")) {
                    methods.collapse.apply(this);
                } else {
                    methods.expand.apply(this);
                }
            } else {
                if ((read_data(wrapper_id) === "collapsed")) {
                    methods.collapse.apply(this);
                } else {
                    methods.expand.apply(this);
                }
            }
        },
        expand : function () {
            var parent = $(this).parents('div.portletWrapper');
            parent.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideDown();
                }
            });
            save_data(parent.attr('id'), 'expanded');
            return this;
        },
        collapse : function () {
            var parent = $(this).parents('div.portletWrapper');
            parent.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideUp();
                }
            });
            save_data(parent.attr('id'), "collapsed");
            return this;
        },
        toggle : function () {
            var parent = $(this).parents('div.portletWrapper'),
                parent_id = parent.attr('id');
            parent.find('dd').each(function () {
                if(!$(this).hasClass("portletFooter")) {
                    $(this).slideToggle();
                }
            });
            if (read_data(parent_id) === "expanded") {
                save_data(parent_id, "collapsed");
            } else {
                save_data(parent_id, "expanded");
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