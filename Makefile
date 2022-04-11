.PHONY: clean format

help:
	@echo "clean - remove junk files and caches"
	@echo "format - format all the files"

clean:
	rm -rf ./assets/dist/
	rm -rf ./.mypy_cache/
	rm -rf ./.parcel-cache/
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

format:
	yarn format
