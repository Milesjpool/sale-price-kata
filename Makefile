include config.env

.PHONY: default
default:
	@echo "Make options:"
	@echo " start"
	@echo " build"
	@echo " startCanary"
	@echo " buildCanary"
	@echo " test"
	@echo " functionalTest"
	@echo " installTestRequirements"


.PHONY: installTestRequirements
installTestRequirements:
	@echo "Installing test requirements"
	sudo pip install -r test_requirements.txt

.PHONY: unitTest
unitTest:
	@echo "Running unit tests...\n"
	@python -m unittest discover -s tests/unit

.PHONY: cleanCanary
cleanCanary:
	@docker image rm -f $(TEST_BUILD) || true

.PHONY: buildCanary
buildCanary: cleanCanary
	@docker build --tag $(TEST_BUILD) .

.PHONY: promoteRelease
promoteRelease:
	@docker tag $(TEST_BUILD) $(RELEASE_BUILD)

.PHONY: functionalTest
functionalTest:
	@echo "Running functional tests...\n"
	@python -m unittest discover -s tests/functional

.PHONY: test
test: unitTest buildCanary functionalTest

.PHONY: build
build: test promoteRelease

.PHONY: startCanary
startCanary: unitTest buildCanary
	@docker run --rm --name $(API_NAME) --expose $(PORT) -p $(PORT):$(PORT) $(TEST_BUILD) $(START_COMMAND) $(DATA_FILE)

.PHONY: start
start: build
	@docker run --name $(API_NAME) --expose $(PORT) -p $(PORT):$(PORT) $(RELEASE_BUILD) $(START_COMMAND) $(DATA_FILE)