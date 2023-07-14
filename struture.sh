#!/bin/bash

rm -rf /test/*
BASEDIR=/test/game
mkdir -p $BASEDIR/{sound,graphic}
touch $BASEDIR/__init__.py
touch $BASEDIR/{sound,graphic}/__init__.py
