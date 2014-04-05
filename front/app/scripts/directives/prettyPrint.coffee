'use strict'

angular.module('frontApp')
  .directive('prettyPrint', (Prettify) ->
    template: '<pre></pre>'
    restrict: 'E'
    link: (scope, element, attrs) ->
      lineNumber = false
      if attrs.linenumber
        lineNumber = parseInt(attrs.linenumber)
      preElement = Prettify.one(attrs.code, attrs.language, lineNumber)

      element.find("pre").append(preElement)
  )
