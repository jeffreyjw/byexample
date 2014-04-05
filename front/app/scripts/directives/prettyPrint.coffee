'use strict'

angular.module('frontApp')
  .directive('prettyPrint', (Prettify) ->
    template: '<pre></pre>'
    restrict: 'E'
    link: (scope, element, attrs) ->
      preElement = Prettify.one(attrs.code, attrs.language, 2)

      element.find("pre").append(preElement)
  )
