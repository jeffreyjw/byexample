'use strict'

describe 'Directive: prettyPrint', () ->

  # load the directive's module
  beforeEach module 'frontApp'

  scope = {}

  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()

  it 'should make hidden element visible', inject ($compile) ->
    element = angular.element '<pretty-print></pretty-print>'
    element = $compile(element) scope
    expect(element.text()).toBe 'this is the prettyPrint directive'
