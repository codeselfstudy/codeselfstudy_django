.PHONY: clean test start

help:
	@echo "clean - remove junk files"
	@echo "test - run pytest"
	@echo "start - start gunicorn in production"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

# -n 3 means run in parallel on three cores
# -x means stop after first test fail
# --lf means run only the last failing test
# --ff means run the fail tests first
# pytest -n 3 --cov-config=.coveragerc -x --lf
test:
	pytest -n 2 -x --lf

# TODO: install New Relic if we use this
start:
	make clean
	NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program supervisord -c supervisord.conf
