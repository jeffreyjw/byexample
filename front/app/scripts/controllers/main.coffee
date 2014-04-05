'use strict'

angular.module('frontApp')
  .controller 'MainCtrl', ($scope, Backend, Prettify) ->

    $scope.documentation = {}


    $scope.init = () ->
      Backend.getDocumentation(
        (data) ->
          $scope.documentation = data
          Prettify.run()
      )


    $scope.init()

