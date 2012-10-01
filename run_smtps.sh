#!/bin/sh

# run_smtps.sh
# Start the smtp server as user daemon 
# and log the stderr and stout

smtps=`pwd`

while true
do
    logfile=`date +%Y%m%d`
    export PYTHONPATH=$PYTHONPATH:$smtps:$smtps/server:$smtps/utils:$smtps/agents; python -c 'import smtp_server; smtp_server.start()' >> /tmp/pseudo_smtp_$logfile.log 2>&1
done

