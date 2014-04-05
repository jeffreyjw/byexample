'use strict'

describe 'Service: Prettify', () ->

  # load the service's module
  beforeEach module 'frontApp'

  # instantiate service
  Prettify = {}
  beforeEach inject (_Prettify_) ->
    Prettify = _Prettify_

  it 'should do something', () ->
    expect(!!Prettify).toBe true
