#!/bin/bash

virtualenv .
rc=$?
if [[ $rc != 0 ]] ; then
	echo "This script requires virtualenv."
	exit 1
fi
source bin/activate
pip install sentry
pip install ../

echo
echo
echo "Next steps:"
echo " 1. Run "
echo "    - Run 'source/bin/activate' to activate the virtualenv."
echo "    - Run 'bin/sentry --config=sentry.conf.py start' to start sentry"
echo " 2. Open another shell and"
echo "    - Run 'source/bin/activate'"
echo "    - Run 'bin/sentry --config=sentry.conf.py send_fake_data'"
echo "    - Hint: Hit Ctrl-C to stop populating the database with fake data."
echo " 3. Open http://localhost:9000"
echo
