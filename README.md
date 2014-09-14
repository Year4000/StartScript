PyStart
=======

This script was made to run the servers at [Year4000].
This script can manage many tasks at once.
You can start/stop/restart each or all tasks using this script,
this script will grow upon needs for the servers at [Year4000].

Install
-------
    * Copy/Move the script "pystart" to "/etc/init.d"
        > `sudo mv pystart /etc/init.d`

    * Copy/Move the settings "tasks.json" to "~/"
        > `mv tasks.json ~/`

    * Edit the config/int script options for your server(s)
        > VIM: `sudo vim /etc/init.d/pystart`
        > Nano: `sudo nano /etc/init.d/pystart`
        > VIM: `vim ~/tasks.json`
        > Nano: `nano ~/tasks.json`

    * Make the script "year4000" executable
        > `sudo chmod +x pystart`

    * Have the script start and stop on system boot and halt
        > CentOS: `sudo chkconfig --add pystart`
        > Debian / Ubuntu: `sudo update-rc.d pystart defaults`

Using
-----
    By appending an number the script will try to run the script for that
    setting suplied above.

    * Start all the tasks
        > sudo service pystart start

    * Stop the tasks
        > sudo service pystart stop

    * Check the status of the tasks
        > sudo service pystart status

    * Restart the tasks
        > sudo service pystart restart

License
------
This script is licensed under the [GNU General Public License][license], version 3.
Copyright &copy; 2014 Year4000 [http://www.year4000.net/][Year4000]

[license]: https://www.gnu.org/licenses/gpl-3.0.txt
[year4000]: https://www.year4000.net/
