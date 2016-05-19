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

	function factory(min, max) {
		if(min < 0 || max <= min) throw new Error("Check : min > 0 && max > min");
		return new api(min, max);
	}

	function api(min, max) {
		this.min = min;
		this.max = max;

		this.scale = function(xMin, xMax, yMin, yMax, value) {

			//check arguments
			if(xMin < 0 || xMax <= xMin) throw new Error("Check : xMin > 0 && xMax > xMin");
			if(yMin < 0 || yMax <= yMin) throw new Error("Check : yMin > 0 && yMax > yMin");
			if(value < xMin || value > xMax) throw new Error("Check : rangeMin <= value <= rangeMax");

			return (yMax - yMin) / (xMax - xMin) * (value - xMin) + yMin;

		}

		this.random = function(min, max) {
			var val = Math.random() * (max - min) + min;
			return val;
		}

	}

	api.prototype.number = function() {
		if(typeof this.logic === 'function') {
			var value = this.random(this.domainMin, this.domainMax);
			var y = this.logic(value);
			var result = this.scale(this.rangeMin, this.rangeMax, this.min, this.max + 1, y);
			if(this.isReverse) {
				result = this.max - result + this.min + 1;
			}
			return result;
		}
		else {
			return this.random(this.min, this.max + 1);
		}
	}

	api.prototype.next = function() {
		return this.number();
	}

	api.prototype.nextInt = function() {
		return Math.floor(this.number());
	}

	api.prototype.transform = function(logic, domainMin, domainMax) {

		//check arguments
		if(domainMin < 0 || domainMax <= domainMin) throw new Error("Check : domainMin >= 0 && domainMax > domainMin");

		this.logic = logic;
		this.domainMin = domainMin;
		this.domainMax = domainMax;
		this.rangeMin = logic(domainMin);
		this.rangeMax = logic(domainMax);

		if(this.rangeMin < 0 || this.rangeMax <= this.rangeMin) throw new Error("Check : logic(domainMin) >= 0 && logic(domainMax) > logic(domainMin)");

		return this;
	}

	api.prototype.reverse = function() {
		this.isReverse = typeof this.isReverse === 'undefined' ? true : !this.isReverse;
		return this;
	}

	api.prototype.slopeTransform = function() {
		return this.transform(function(x) { return Math.log(x) / Math.log(2); }, 1, 2);
	}

	api.prototype.slopeReverseTransform = function() {
		return this.transform(function(x) { return Math.log(x) / Math.log(2); }, 1, 2).reverse();
	}

	api.prototype.concaveSlopeTransform = function() {
		return this.transform(function(x) { return Math.sin(x) }, 0, Math.PI / 2);
	}

	api.prototype.concaveSlopeReverseTransform = function() {
		return this.transform(function(x) { return Math.sin(x) }, 0, Math.PI / 2).reverse();
	}

	api.prototype.hourglassTransform = function() {
		return this.transform(function(x) { return Math.cos(x) + 1 }, Math.PI, Math.PI * 2);
	}

	api.prototype.dTransform = function() {

		return this.transform(function(x) {
			if(x <= Math.PI / 2) {
				return Math.sin(x);
			}
			else {
				return Math.sin(x) * (-1) + 2;
			}
		}, 0, Math.PI)

	}

	api.prototype.squareTransform = function() {
		return this.transform(function(x) { return x * x; }, 0, 2);	
	}

	return factory;
}));
