/*!
 * JavaScript Log Random
 * https://github.com/haloper/js-object-wrapper
 *
 * Released under the MIT license
 */
(function (factory) {
	'use strict';
	if (typeof define === 'function' && define.amd) define(factory); //for AMD(RequireJS)
	else if (typeof exports === 'object') module.exports = factory(); //for CommonJS
	else {
		var oldRandom = window.Random;
		var random = window.Random = factory();

		random.noConflict = function () {
			window.Random = oldRandom;
			return random;
		};
	}
}(function () {
	'use strict';

	function factory() {
		if(arguments.length === 2) return randomFloor(arguments[0], arguments[1]);
		if(arguments.length === 3) return randomLog(arguments[0], arguments[1], arguments[2]);
		return new Error("Wrong arguments!!!");
	}

	function random(min, max) {
		return Math.random() * (max - min + 1) + min;
	}

	function randomFloor(min, max) {
		return Math.floor(random(min, max));
	}
	
	//logRange > 1
	function randomLog(min, max, logRange, a) {

		a = typeof a === 'undefined' ? 2 : a;

		if(logRange <= 1) throw new Error("logRange argument have to be more than 1");

		var logMax = log(logRange + 1, a);

		var x = log(random(1, logRange), a); //0 ~ logMax

		var y = ((max - min + 1) / logMax) * x + min; //min ~ max

		return Math.floor(y);
	}

	function log(val, a) {
		return Math.log(val) / Math.log(a);
	}

	return factory;
}));
