/*global describe, it */
'use strict';

var expect = expect || {};

(function () {
    describe('Project suite', function () {
        describe('Test numbers', function () {
            describe('Deeper', function () {
                //<
                it('should be equal to 6', function () {
                    expect(6).to.eql(6);
                });
                //>
            });

            //< @requires
            it('should be equal to 5', function () {
                expect(5).to.eql(7);
            });
            //>

            //<
            it('should be equal to 4', function () {
                expect(4).to.eql(4);
            });
            //>

            //<
            it('should be equal to 3', function () {
                expect(3).to.eql(3);
            });
            //>
        });
    });
})();
