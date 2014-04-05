'use strict'

angular.module('frontApp')
  .controller 'GlobalCtrl', ($scope, $location) ->


    $scope.location = $location
