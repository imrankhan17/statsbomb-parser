#!/usr/bin/env bash

rm -rf build dist *.egg-info
docker run -it --rm -v $(pwd):/home -w /home statsbomb-parser python setup.py sdist bdist_wheel
docker run -it --rm -v $(pwd):/home -w /home statsbomb-parser python -m twine upload dist/*
