# GBPX

The code will record the value of GBP against 15 other currencies.
Its is written very badly in python.

## Install

Work in progress.

```bash
git clone https://github.com/lightatzero/gbpx.git
sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install sphinx
pip install flake8
```

## Usage

```bash
./gbpx.py &
cat gbp*
```

## Tests

Run all tests
```bash
python -m unittest discover
```

Run a single Tests
```bash
python -m unittest test.testunits
```

## Linting

Check style
```bash
flake8 *.py test/*.py
```


## Build Documentation 

```bash
cd docs
make html
```

Open the following in a browser:
gbpx/docs/_build/html/index.html 

## Contributing
Please open an issue to discuss changes.

## License
[MIT](https://choosealicense.com/licenses/mit/)
