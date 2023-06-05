install:
	poetry install

lint:
	poetry run flake8 tasks_for_rabbitmq

consumer:
	poetry run consumer

publisher:
	poetry run publisher

file_generation:
	poetry run file_generation

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

.PHONY: install lint consumer publisher consumer publisher file_generation build publish package-install package-reinstall