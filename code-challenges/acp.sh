#!/bin/bash

pushtogit(){
    git add .
    read -p "commit message: " message
    git commit -m "$message"
    git push origin main
    echo
    
    git status
}
pushtogit