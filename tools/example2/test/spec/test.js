/*global describe, it */
'use strict';
(function () {
    describe('Project suite', function () {
        describe('Test numbers', function () {
            it('should be equal to 5', function () {
                expect(5).to.eql(5)
            });
            it('should be equal to 4', function () {
                expect(4).to.eql(4)
            });
            it('should be equal to 3', function () {
                expect(3).to.eql(3)
            });
        });
    });
})();
