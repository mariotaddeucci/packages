#!/bin/bash
cwd=$(pwd)
cd "$(dirname "$0")"/..

if [[ $(python -c 'import sys; print(sys.version_info[:3][0])') = 2 ]]; then
  alias python=python3
fi

echo Installing tests dependencies
python -m pip install -r requirements-dev.txt &> /dev/null

echo Running isort
python -m isort . &> /dev/null

echo Running Black auto lint
python -m black . &> /dev/null

cd ${cwd}
