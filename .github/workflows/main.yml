name: Github Action Tutorials
on:
  push:
    branches:
      - master
      - main
  workflow_dispatch:
    inputs:
      Environments:
        type: choice
        default: dev
        options:
          - dev
          - stage
          - prod
          - preprod
          - uat
jobs:
  Development:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: app01
    outputs:
      Job_Id: "First Job"
    steps:
      - id: "A"
        name: Checkout Repository
        uses: actions/checkout@v4
      - id: "Github"
        name: Github
        env:
          CUSTOM_GITHUB: ${{ toJson(github) }}
        run: echo $CUSTOM_GITHUB
          
  Stage:
    runs-on: windows-latest
    needs: Development
    defaults:
      run:
        working-directory: app01
    env:
      Username: "Justice Owusu Boateng"
      Password: "This is my current password"
    steps:
      - id: "ACheckoutRepo"
        name: Checkout repo
        uses: actions/checkout@v4
      - id: DisplayValueFromOthers
        name: Display values from others
        run: |
          echo "${{ needs.Development.outputs.Job_Id}}"
          echo "This is Username 1: ${{ vars.USERNAME }}"
          echo "This is Username 2: ${{ vars.USERNAME2 }}"
          echo "This is PASSWPRD 1: ${{ secrets.PASSWORD1 }}"
          echo "This is PASSWORD 2: ${{ secrets.PASSWORD2 }}"