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
```

## Usage

```bash
./exchangeScraper.py &
cat gbp*
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
