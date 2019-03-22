#!/bin/bash

if [ -z "$1" ]; then
    git commit -a -m "update solutions"
else
    git commit -a -m "$1"
fi