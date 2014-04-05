'use strict'

angular.module('frontApp')
  .service 'Prettify', () ->

    run: () ->
      prettyPrint()

    one: (src, language, lineNumber) ->
      return prettyPrintOne(src, language, lineNumber)
