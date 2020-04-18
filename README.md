# Ultimate Schedule API

![Python application](https://github.com/skhortiuk/asu-schedule/workflows/Python%20application/badge.svg?branch=master)

## About
As far as you know, a lot of universities uses the "ПС-Розклад" system to share schedule among the students.
It's really good when you're the user, not developer. Many developers/students want to use schedule from mentioned 
resource to build more useful/powerful interfaces, such as mobile apps, telegram bots, etc.
But there's no such API. **So, we've solved the problem.** 

## Blueprints
```
/groups
    /
    /exists

/teachers
    /
    /exists

/faculties
    /
    /exists

/schedule
    /groups
    /teachers
```

## Usage
You can specify URL to whatever schedule you want if it uses the "ПС-Розклад" system. 
Just pass the URL to the `X-Schedule-Url` header.
