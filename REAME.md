# TAXI APP

## TODO

- docker
    - [ ] push both master & dev branch image to ECR, tag them by git tag(version)
- git
    - [ ] create master & dev branch
- django
    - [x] swagger
    - [x] add api version for both api & swagger
    - [ ] survey if spectacular support drf nested route, since yasg is kinda buggy on url path arg
    - [ ] survey if jwt is realy necessary
    - [ ] social media oauth2 (google, line)
- nginx
    - [ ] update config
    - [ ] ssl?
- react
    - [ ] social media oauth2 (google, line)


## other
### command to check database connection
python manage.py check --database default
