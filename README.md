# px-notifier
name: Deploy to Cloud Foundry

on:
  push:
    branches:
    - main

jobs:
  build:
    runs-on: ubuntu-22.04

  deploy:
    runs-on: ubuntu-22.04
    needs: build
    
    steps:
    - uses: joekrom/px-notifier@main
      with:
        smtp_address: "smtp.office365.com"
        smtp_port: "587"
        username: "notify@gmail.com"
        password: "xxxxxxx"
        subject: "pipeline name"
        ssl: "true"
        from: "notify@gmail.com"
        to: "johndoe@yahoo.fr,marydoe@yahoo.fr"
        body: "testing body"
