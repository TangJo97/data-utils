#!/usr/bin/env sh

activate (){
    # . ./env/Scripts/activate # when I do this, it will source activate, which 
    # will replace my current source of this file. 
    poetry shell
}

dev_setup(){
    pip install nox==2022.1.7
    poetry install
}

format (){
    echo "############### Formatting ###############"""
    poetry run black . -v
}

sort_import(){
    echo "############### Performing Isort ###############"""
    poetry run isort .
}

clean_import(){
    echo "############### Removing unused imports ###############"""
    poetry run pycln . --config pyproject.toml
}

compliance(){
    echo "############### Checking PEP8 compliance ###############"""
    poetry run flake8 .
}

all_tests(){
    echo "############### Start Testing environments ###############"
    nox --session tests
}

building(){
    echo "############### Building the Project ###############"
    poetry build
}

all_checks (){
    clean_import && sort_import && format && compliance  # && is to make sure that if one fail
    # everything fails
}

ignore-pre-commit(){
    git commit --no-verify -m "$1"
}

publish(){
    all_tests && all_checks && building && echo"" && echo "Don't forget to Git your files"
}