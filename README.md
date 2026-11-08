# jenkins-ci-demo

**Author:** Bella Lopez

A small Python project used to practice Continuous Integration with Jenkins and GitHub webhooks (CMSC 426, In-Class Activity #3).

## What it does

`app.py` has a function, `add_numbers(a, b)`, that returns the sum of two numbers. The tests in `tests/` check that it works.

## Run the app

```
python app.py
```

## Run the tests

```
python -m unittest discover -s tests
```

A passing run ends with `OK`.

## How the CI works

Pushing to the `main` branch triggers a GitHub webhook. The webhook notifies Jenkins, which runs the tests in the `Student-CI-Project` job and reports a pass or fail result.