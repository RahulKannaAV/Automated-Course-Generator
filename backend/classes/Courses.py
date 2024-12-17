
class Courses:
    def __init__(self, db_tuple):
        self.__course_id = db_tuple[0]
        self.__course_name = db_tuple[1]
        self.__video_id = db_tuple[2]
        self.__generated_date = db_tuple[3]
        self.__completed = db_tuple[4]

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_video_id(self):
        return self.__video_id

    def get_generated_date(self):
        return self.__generated_date

    def get_completion_status(self):
        return self.__completed

