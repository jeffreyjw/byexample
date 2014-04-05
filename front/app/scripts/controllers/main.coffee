'use strict'

angular.module('frontApp')
  .controller 'MainCtrl', ($scope, Backend, Prettify) ->

    $scope.documentation = {}
    $scope.documentationArray = []
    $scope.selectedArticle = null


    $scope.setArticle = (title) ->
      $scope.selectedArticle = title


    $scope.documentationAsArray = () ->
      $scope.documentationArray = []
      for title of $scope.documentation.documentation
        obj = { title: title, article: $scope.documentation.documentation[title] }
        $scope.documentationArray.push obj


    $scope.init = () ->
      Backend.getDocumentation(
        (data) ->
          $scope.documentation = data
          $scope.documentationAsArray()
          $scope.selectedArticle = 0

          Prettify.run()
      )


    $scope.init()

