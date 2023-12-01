#!/bin/bash

pushtogit(){
    git add .
    read -p "commit message: " message
    git commit -m "$message"
    git push
# i want to insert line break here
    git status
}
pushtogit