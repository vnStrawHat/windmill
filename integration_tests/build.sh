#!/bin/bash
set -euo pipefail
script_dirpath="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root_dirpath="$(cd "${script_dirpath}/.." && pwd)"

source ${script_dirpath}/.env

docker pull ${WM_IMAGE}:${WM_VERSION}

if [[ ${WM_VERSION_DEV} = *-dev ]]; then
  echo "Building dev docker image locally..."
  previous_version=$(cat ${root_dirpath}/version.txt)
  echo "Previous version was: ${previous_version}"
  ${root_dirpath}/.github/change-versions.sh ${WM_VERSION_DEV}
  docker build -t ${WM_IMAGE}:${WM_VERSION_DEV} \
    -f ${root_dirpath}/Dockerfile ${root_dirpath}
  ${root_dirpath}/.github/change-versions.sh ${previous_version}
else 
  docker pull ${WM_IMAGE}:${WM_VERSION_DEV}
fi
