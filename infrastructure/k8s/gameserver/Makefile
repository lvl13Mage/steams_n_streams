deploy-production:
	kubectl config use-context magecloud
	kubectl apply -k overlays/production

destroy-production:
	kubectl config use-context magecloud
	kubectl delete -k overlays/production

deploy-development:
	kubectl config use-context magecloud
	kubectl apply -k overlays/development

destroy-development:
	kubectl config use-context magecloud
	kubectl delete -k overlays/development

deploy-local:
	kubectl config use-context rancher-desktop
	kubectl apply -k overlays/development

destroy-local:
	kubectl config use-context rancher-desktop
	kubectl delete -k overlays/development

	