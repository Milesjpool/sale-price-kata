.PHONY: test

default:
	@echo "Make options:"
	@echo " test"
	@echo " functionalTest"
	@echo " installTestRequirements"

installTestRequirements:
	@echo "Installing test requirements"
	sudo pip install -r test_requirements.txt

functionalTest:
	@echo "Running functional tests...\n"
	@python -m unittest discover -s tests/functional

test: functionalTest
