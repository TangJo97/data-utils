#!/usr/bin/env sh

activate (){
    . ./env/Scripts/activate # when I do this, it will source activate, which 
    # will replace my current source of this file. 
}

format (){
    black ./
}

all_tests (){
    coverage run -m unittest discover -v tests
    coverage report -m --omit="*/tests/*"
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

publish(){
    echo "Did you run 'nox --session tests' first? [y/n]"
    read response
    if [[ $response == "n" ]]
    then
        echo "Stopping the publishing"
        return
    fi
    all_tests
    all_checks
    echo "############### Building the Project ###############"
    python -m build .
    echo "Don't forget to Git your files"
}