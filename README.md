# geodjango: Simple api


## Installation

1. Install python 3.7.1

2. Create a virtualenv (use `virtualenvwrapper`):

        mkvirtualenv geodjango

3.  Install requirements via `pip`:

        make requirements-development

4.  Run the project:

        make runserver-development


## Tests


To run the test suite, execute:

    make test

It may take a while to run all tests. To run specific testcases, use the
following command:

    make test-matching Q=keyword_matching_method_name


## End-to-End / Acceptance Testing


We use Behave to do acceptance tests. To run the acceptance test
suite, execute:

    make test-acceptance


## Create new release


We use `bumpversion` to generate new releases, following the base
principles of [SEMVER](http://semver.org/).

-   Patch [ X.X.0 to X.X.1 ] :

        make release-patch

-   Minor [ X.0.X to X.1.X ] :

        make release-minor

-   Major [ 0.X.X to 1.X.X ] :

        make release-major

## Install with Docker

        docker-compose up
        browser http://localhost:8000/