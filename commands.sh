#!/usr/bin/env sh

activate (){
    . ./env/Scripts/activate # when I do this, it will source activate, which 
    # will replace my current source of this file. 
}

format (){
    black ./
}

all_tests (){
    python -m unittest discover -v tests
}

all_checks (){
    echo "############### Performing Isort ###############"""
    isort .
    echo "############### Removing unused imports ###############"""
    pycln . --config pyproject.toml
    echo "############### Formatting ###############"""
    black .
    echo "############### Checking PEP8 compliance ###############"""
    flake8 .
}

ignore-pre-commit(){
    git commit --no-verify -m "$1"
}