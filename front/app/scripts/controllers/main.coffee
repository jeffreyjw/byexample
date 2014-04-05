'use strict'

angular.module('frontApp')
  .controller 'MainCtrl', ($scope, Backend, Prettify) ->

    $scope.documentation = {}
    $scope.selectedArticle = null


    $scope.setArticle = (title) ->
      $scope.selectedArticle = title


    $scope.init = () ->
      Backend.getDocumentation(
        (data) ->
          $scope.documentation = data

          for article of $scope.documentation.documentation
            $scope.selectedArticle = article
            break

          Prettify.run()
      )


    $scope.init()

