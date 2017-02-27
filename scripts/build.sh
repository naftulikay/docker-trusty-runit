#!/bin/bash

set -e

export DEBIAN_FRONTEND=noninteractive

function install-packages() {
  local packages=runit

  log "installing packages..."
  apt-get update >/dev/null
  apt-get install -y ${packages} >/dev/null
}

function clean() {
  log "cleaning up..."
  apt-get clean >/dev/null
  # remove this script
  test -f /build && rm -f /build
}

function main() {
  install-packages
  clean
}

function log() {
  echo "[build]" $@
}

function error() {
  echo $@ >&2
  exit 1
}

if [[ ${BASH_SOURCE[0]} == $0 ]]; then
   main
fi
