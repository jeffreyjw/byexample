'use strict'

angular.module('frontApp')
  .service 'Backend', ($http) ->
    # AngularJS will instantiate a singleton by calling "new" on this function

    url = ""

    headers = {
      "Content-Type": "application/x-www-form-urlencoded"
    }


    request: (resource, method, data, callback, errorCallback) ->
      req = {
        url: url + resource,
        method: method,
        headers: headers
      }

      lowerMethod = method.toLowerCase()
      if lowerMethod == "get" || lowerMethod == "delete"
        req.params = data
      else if lowerMethod == "post" || lowerMethod == "put"
        req.data = $.param(data)

      $http(req).success(
        (data) ->
          if callback != null
            callback data
      ).error(
        (data) ->
          if errorCallback != null
            errorCallback data
      )


    getDocumentation: (callback=null, errorCallback=null) ->
      this.request(
        "documentation.json", "GET", {},
        callback, errorCallback
      )


