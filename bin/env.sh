
DOCKER_HOME=$HOME/creist/Projects/docker_mysql_flask_sv/docker-mysql
#DOCKER_HOME=$HOME/projects/docker_mysql_flask_sv/docker-mysql

IFS=$'\n'
for line in `cat $DOCKER_HOME/.env`
do
	export $line
done 
