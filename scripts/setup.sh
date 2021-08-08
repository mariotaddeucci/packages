#!/bin/bash
cwd=$(pwd)
cd "$(dirname "$0")"
git config advice.ignoredHook false
[ -e ../.git/hooks/pre-commit ] && rm -- ../.git/hooks/pre-commit
cp -p _pre-commit ../.git/hooks/pre-commit
cd ${cwd}
