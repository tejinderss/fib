# Fib

Fib is a Flask application to generate the api to provide the fibonacci sequence

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)

It is strongly recommended to also install and use the following tools:

1. [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)
2. [virtualenvwrapper](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenvwrapper)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone https://github.com/tejinderss/fib.git
    $ cd fib

#### 2. Create and initialize virtualenv for the project:

    $ mkvirtualenv fib
    $ pip install -r requirements.txt

#### 3. Install the fib package so that tests could locate it:

    $ pip install .

#### 4. Run the development server:

    $ FLASK_APP=fib/fib.py flask run

#### 5. Open [http://localhost:5000/fib/5](http://localhost:5000/fib/5)


### Development

If all went well in the setup above you will be ready to start hacking away on
the application.


#### Tests

To run the tests use the following command:

    $ python tests/test_fib.py
