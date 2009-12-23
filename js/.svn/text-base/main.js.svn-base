/*
 * Mobile Ajax Inspired by Jquery
 * This version of Jquery is modified to run on mobile devices
 */



var mQuery = window.mQuery = window.$ = function( selector ) {
	
	console.log('test')
	// The jQuery object is actually just the init constructor 'enhanced'
	return new jQuery.fn.init( selector, context );
};

// A simple way to check for HTML strings or ID strings
// (both of which we optimize for)
var quickExpr = /^[^<]*(<(.|\s)+>)[^>]*$|^#([\w-]+)$/,

// Is it a simple selector
	isSimple = /^.[^:#\[\.]*$/,

// Will speed up references to undefined, and allows munging its name.
	undefined;
	jQuery.fn = jQuery.prototype = {
		init: function( selector, context ) {
			// Make sure that a selection was provided
			selector = selector || document;

			// Handle $(DOMElement)
			if ( selector.nodeType ) {
				this[0] = selector;
				this.length = 1;
				return this;
			}
		}
}