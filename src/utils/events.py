class Event:
    def __set_name__(self, owner, name):
        self.name = " ".join(name.split("_")).title()

    def __get__(self, instance, owner):
        return self.name


class Events:
    GET_ALL_FACULTIES = Event()
    IS_FACULTY_EXISTS = Event()
    GET_ALL_GROUPS = Event()
    IS_GROUP_EXISTS = Event()
    GET_ALL_TEACHERS = Event()
    IS_TEACHER_EXISTS = Event()
    GET_GROUPS_SCHEDULE = Event()
    GET_TEACHERS_SCHEDULE = Event()
    GET_DOCS = Event()
