.PHONY: build
build:
	pip uninstall -y GRPC-server
	python setup.py bdist_wheel
	pip install dist/*.whl