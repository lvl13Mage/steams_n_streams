dev-deploy:
	cd infrastructure/k8s/gameserver && make deploy-local

dev-build:
	docker build -t steamsnstreams_gameserver:local-latest gameserver

dev: dev-build dev-deploy