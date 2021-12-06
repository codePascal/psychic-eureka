#!/usr/bin/env bash
#
##############################################################################
# run
#
# Execute this shell script inside the repository. The argument denotes the
# project number, that will be solved. If a problem is not implemented yet, a
# 'NotImplementedError' will arise.
#
# Usage example:
# bash run.sh 1
#
###############################################################################

python3 projects/project_euler_$1.py