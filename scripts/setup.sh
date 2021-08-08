#!/bin/bash
cwd=$(pwd)
cd "$(dirname "$0")"
echo . ./pre_commit.sh > ../.git/hooks/pre-commit.sh
cd ${cwd}
