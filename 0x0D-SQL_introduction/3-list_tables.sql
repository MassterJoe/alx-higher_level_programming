-- This script lists all the tables in msql database
dbname="$1"
-- Build the MySQL command to list tables
mysql_cmd="USE ${dbname}; SHOW TABLES;"
-- Run the MySQL command and display the results
mysql -e "${mysql_cmd}"
