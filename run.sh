#!/bin/bash
docker run \
  -v "$PWD":/usr/src/myapp \
  -w /usr/src/myapp \
  -u $(id -u):$(id -g) \
  --rm \
  generate-covid-visualization
