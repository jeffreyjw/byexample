/*global describe, it */
'use strict';

var expect = expect || {};

(function () {
    describe('Project suite', function () {
        describe('Test booleans', function () {

            //<@article Beginner booleans
            it('should be true', function () {
                expect(true || false).to.eql(true);
            });
            //>

            //< @article Beginner booleans
            it('should be false', function () {
                expect(true && false).to.eql(false);
            });
            //>
        });
    });
})();
