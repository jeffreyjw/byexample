'use strict'

angular.module('frontApp')
  .controller 'DashboardCtrl', ($scope, Backend) ->


    $scope.documentation = null
    $scope.tableData = []


    $scope.getTableData = (doc) ->
      $scope.tableData = [
        { key: "Last tested", value: doc.stats.end },
        { key: "Tests", value: doc.stats.tests },
        { key: "Passed", value: doc.stats.passes },
        { key: "Failed", value: doc.stats.failures },
      ]


    $scope.init = () ->
      Backend.getDocumentation(
        (data) ->
          $scope.documentation = data
          $scope.getTableData(data)
      )


    $scope.init()
