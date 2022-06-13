.PHONY: conform

conform	: ## Conform to a standard of coding syntax
	isort --profile black app01 app02
	find app01 -name "*.json" -type f  -exec sed -i '1s/^\xEF\xBB\xBF//' {} +
	find app02 -name "*.json" -type f  -exec sed -i '1s/^\xEF\xBB\xBF//' {} +
