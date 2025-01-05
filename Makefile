DC = docker compose
APP_FILE = docker_compose/app.yaml
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER =  example-db
APP_CONTAINER = main-app
ENV = --env-file .env
MANAGE_PY = python manage.py

.PHONY: storages
storages-start:
	${DC} -f ${STORAGES_FILE} up -d

.PHONY: storages-drop
storages-drop:
	${DC} -f ${STORAGES_FILE} down

.PHONY: storages-logs
storages-logs:
	${DC} -f ${STORAGES_FILE} logs -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: app-start
app-start:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-drop
app-drop:
	${DC} -f ${APP_FILE} down

.PHONY: app-logs
app-logs:
	${DC} -f ${APP_FILE} logs -f

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: createsuperuser
createsuperuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic


.PHONY: run-test
run-test:
	${EXEC} ${APP_CONTAINER} pytest