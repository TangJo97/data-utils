#!/usr/bin/env sh

activate (){
    . ./env/Scripts/activate # when I do this, it will source activate, which 
    # will replace my current source of this file. 
}

format (){
    black main/
    black tests/
}

all_tests (){
    python -m unittest discover -v tests
}

ignore-pre-commit(){
    git commit --no-verify -m "$1"
}