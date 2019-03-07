#!/bin/sh

TRIBE=$1

echo 'Clearing tables from $TRIBE...'
python ../manage.py migrate $TRIBE zero

echo 'Rewriting tables for $TRIBE...'
python ../manage.py migrate $TRIBE

