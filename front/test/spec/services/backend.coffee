'use strict'

describe 'Service: Backend', () ->

  # load the service's module
  beforeEach module 'frontApp'

  # instantiate service
  Backend = {}
  beforeEach inject (_Backend_) ->
    Backend = _Backend_

  it 'should do something', () ->
    expect(!!Backend).toBe true
