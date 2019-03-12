.PHONY: test

default:
	@echo "Make options:"
	@echo " test"
	@echo " functionalTest"

functionalTest:
	python -m unittest discover -s tests/functional

test: functionalTest
