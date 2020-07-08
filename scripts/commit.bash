#!/bin/bash

pip freeze > requirements.txt
git add -A && git commit -m "$1" && git push
