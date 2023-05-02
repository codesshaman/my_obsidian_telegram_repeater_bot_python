name = Zettelkasten Bot

NO_COLOR=\033[0m	# Color Reset
COLOR_OFF='\e[0m'       # Color Off
OK_COLOR=\033[32;01m	# Green Ok
ERROR_COLOR=\033[31;01m	# Error red
WARN_COLOR=\033[33;01m	# Warning yellow
RED='\e[1;31m'          # Red
GREEN='\e[1;32m'        # Green
YELLOW='\e[1;33m'       # Yellow
BLUE='\e[1;34m'         # Blue
PURPLE='\e[1;35m'       # Purple
CYAN='\e[1;36m'         # Cyan
WHITE='\e[1;37m'        # White
UCYAN='\e[4;36m'        # Cyan

all:
	@printf "$(OK_COLOR)==== Launch configuration ${name}... ====$(NO_COLOR)\n"
	@docker-compose -f ./docker-compose.yml up -d

help:
	@echo -e "$(OK_COLOR)==== All commands of ${name} configuration ====$(NO_COLOR)"
	@echo -e "$(YELLOW)  - ______________________MAIN_________________________"
	@echo -e "$(YELLOW)  - make			: Launch configuration"
	@echo -e "$(YELLOW)  - make build			: Building configuration"
	@echo -e "$(YELLOW)  - make conn			: Connect to configuration"
	@echo -e "$(YELLOW)  - make connroot		: Connection from root"
	@echo -e "$(YELLOW)  - make down			: Stopping configuration"
	@echo -e "$(YELLOW)  - make logs			: Show balancer logs"
	@echo -e "$(YELLOW)  - make ps			: Show configuration containers"
	@echo -e "$(YELLOW)  - make re			: Rebuild configuration$(NO_COLOR)"
	@echo -e "$(ERROR_COLOR)   - _____________________CLEAN_________________________"
	@echo -e "$(ERROR_COLOR)   - make clean			: Cleaning configuration$(NO_COLOR)"

build:
	@printf "$(OK_COLOR)==== Building configuration ${name}... ====$(NO_COLOR)\n"
	@docker-compose -f ./docker-compose.yml up -d --build

conn:
	@printf "$(OK_COLOR)==== Connecting to container ${name}... ====$(NO_COLOR)\n"
	@bash scripts/connect.sh

connroot:
	@printf "$(OK_COLOR)==== Connecting with root ${name}... ====$(NO_COLOR)\n"
	@bash scripts/connectroot.sh

down:
	@printf "$(ERROR_COLOR)==== Stopping configuration ${name}... ====$(NO_COLOR)\n"
	@docker-compose -f ./docker-compose.yml down

logs:
	@printf "$(WARN_COLOR)==== Show logs ${name}... ====$(NO_COLOR)\n"
	@bash scripts/logs.sh

ps:
	@printf "$(BLUE)==== View configuration ${name}... ====$(NO_COLOR)\n"
	@docker-compose -f ./docker-compose.yml ps

re:	down
	@printf "$(OK_COLOR)==== Rebuild configuration ${name}... ====$(NO_COLOR)\n"
	@docker-compose -f ./docker-compose.yml up -d --build

clean: down
	@printf "$(ERROR_COLOR)==== Cleaning configuration ${name}... ====$(NO_COLOR)\n"
	@yes | docker system prune -a

fclean:
	@printf "$(ERROR_COLOR)==== Total clean of all configurations docker ====$(NO_COLOR)\n"
#	@docker stop $$(docker ps -qa)
#	@docker system prune --all --force --volumes
#	@docker network prune --force
#	@docker volume prune --force
.PHONY	: all help build down logs conn connroot re ps clean fclean