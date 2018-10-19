#!/bin/bash -xe

easy_install pip
pip install -U tox
pip install -U requests-mock==1.4.0

make check
make unittest
make lint || true

if grep -q 'Fedora' /etc/redhat-release; then
    make unittest3
fi

if git diff-tree --no-commit-id --name-only -r HEAD | egrep --quiet 'ovirt-provider-ovn.spec.in|Makefile|automation' ; then
    ./automation/build-artifacts.sh
fi
