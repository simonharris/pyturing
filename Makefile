
test:
	@python -m pytest -q

testc:
	@coverage run -m pytest -q
	@coverage report --omit="tests/*" -m
