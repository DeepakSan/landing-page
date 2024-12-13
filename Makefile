up:
	docker-compose up -d --build

down:
	docker-compose down

complete-down:
	docker-compose down -v

logs:
	@if [ -z "$(container)" ]; then \
		echo "Error: Please specify the container name to view logs using 'container=<container_name>'"; \
		exit 1; \
	fi
	docker-compose logs -f $(container)

exec:
	@if [ -z "$(container)" ]; then \
		echo "Error: Please specify the container name to view logs using 'container=<container_name>'"; \
		exit 1; \
	fi
	docker exec -it $(container) bash

restart:
	docker-compose restart

stop:
	docker-compose down

rm-containers:
	@if [ -n "$$(docker ps -aq)" ]; then \
		docker rm -f $$(docker ps -aq); \
	else \
		echo "No containers to remove."; \
	fi
	
rm-images:
	docker rmi -f $$(docker images -q)

rm-networks:
	docker network prune -f

rm-volumes:
	docker volume prune -f

clean-all: 
	@echo "Remove all images, containers, networks and volumes..."
	Make stop
	Make rm-containers 
	Make rm-images 
	Make rm-networks 
	Make rm-volumes

migrate:
	@echo "Migrating the PostgreSQL database..."
	docker exec -it application bash -c "flask db upgrade"

backup:
	@echo "Backing up the PostgreSQL database..."
	@mkdir -p data  # Ensure the data directory exists
	@filename=$$(date +%Y%m%d_%H%M%S); \
	docker exec -t database pg_dumpall -c -U deepaksanjaysj > data/backup_$${filename}.sql; \
	echo "Backed up the PostgreSQL database as data/backup_$${filename}.sql."

restore:
	@if [ -z "$(filename)" ]; then \
		echo "Error: Please specify the backup file to restore using 'filename=<your_backup_file>'"; \
		exit 1; \
	fi
	@echo "Restoring the PostgreSQL database from data/$(filename).sql..."
	@docker exec -i database psql -U deepaksanjaysj < data/$(filename).sql
	@echo "Restore complete."

