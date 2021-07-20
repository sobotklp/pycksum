#!/bin/bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PLAT=manylinux1_x86_64
DOCKER_IMAGE=quay.io/pypa/manylinux1_x86_64

# Invoke Docker to build all supported Python binary versions for Linux
# This will create a folder 'wheelhouse' containing the various versions
docker run --rm -e PLAT=$PLAT -v $SCRIPT_DIR:/io $DOCKER_IMAGE /io/travis/build-wheels.sh

# To upload binaries to PyPI:
# twine upload wheelhouse/*
