# make all - Runs `build` target
all: build

# make help - Display callable targets.
help:
	@egrep "^# make" Makefile

# make build - Build packages for distribution.
build:
	@echo "Building Source Distribution files..."
	@python setup.py sdist
	@echo "Building Wheels..."
	@python setup.py bdist_wheel
	@echo

# make publish - Publish packages for PyPi.
publish:
	@echo "Publishing to PyPi..."
	@twine upload dist/*
	@echo

# make clean - Remove previous builds.
clean:
	@echo "Cleaning build directory..."
	@rm -f ./dist/*
	@echo "Removed all previous builds."
	@echo
