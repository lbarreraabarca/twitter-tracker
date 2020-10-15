#!/bin/bash

function qualityCode() {
    pylint -r n --rcfile=src/.pylintrc $1
    status=${PIPESTATUS[0]}
    if [ ${status} -ge 1 ]; then
        echo "pylint exited with code ${status}, check pylint errors"
        exit ${status}
    fi
}

qualityCode src/
qualityCode main.py
exit 0