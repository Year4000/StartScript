Y4K Start Script
======
This script was made to run the servers at [Year4000]. This script can manage
many servers at once. You can start/stop/restart each or all servers
using this script, this script will grow upon needs for the servers at
[Year4000].

Install
------
    - Copy/Move the script "year4000" to "/etc/init.d"
        > sudo mv year4000 /etc/init.d
    - Copy/Move the settings "servers.cfg" to "~/"
        > mv servers.cfg ~/
    - Edit the config/int script options for your server(s)
        > VIM: sudo vim /etc/init.d/year4000
        > Nano: sudo nano /etc/init.d/year4000
        > VIM: vim ~/servers.cfg
        > Nano: nano ~/servers.cfg
    - Make the script "year4000" executable
        > sudo chmod +x year4000
    - Have the script start and stop on system boot and halt
        > CentOS: sudo chkconfig --add year4000
        > Debian / Ubuntu: sudo update-rc.d year4000 defaults

Using
------
    By appending an number the script will try to run the script for that
    setting suplied above.
    - Start all the servers
        > sudo service year4000 start
    - Stop the servers
        > sudo service year4000 stop
    - Check the status of the servers
        > sudo service year4000 status
    - Restart the servers
        > sudo service year4000 restart

License
------
This script is licensed under the [GNU General Public License][license], version 3.
Copyright &copy; 2014 Year4000 [http://www.year4000.net/][Year4000]

[license]: https://github.com/Year4000/start-script/blob/master/LICENSE.md
[year4000]: http://www.year4000.net/
