#! /usr/bin/python3.4

### BEGIN INIT INFO
# Provides:   pystart
# Required-Start: $local_fs $remote_fs $mysqld $mysql $mongo
# Required-Stop:  $local_fs $remote_fs $mysqld $mysql $mongo
# Should-Start:   $network
# Should-Stop:    $network
# Default-Start:  4 5 6
# Default-Stop:   0 1 6
# Short-Description: Python Service Script
# Description: This script is written in python to allow the creation of
#       processes to be ran inside of one tmux session with multiple tabs.
### END INIT INFO

class Server: