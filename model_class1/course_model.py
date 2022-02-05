class Model_course:
    def __init__(self,course_id,course_name,course_description,total_year):
        self.courseid=course_id
        self.coursename=course_name
        self.coursedesc=course_description
        self.year=total_year

    def set_course_id(self,course_id):
        self.courseid=course_id

    def get_course_id(self):
        return self.courseid
    def set_course_name(self,course_name):
        self.coursename=course_name
    def get_course_name(self):
        return self.coursename
    def set_course_description(self,couse_description):
        self.coursedesc=couse_description
    def get_course_description(self):
        return self.coursedesc
    def set_total_year(self,total_year):
        self.year=total_year
    def get_total_year(self):
        return self.year