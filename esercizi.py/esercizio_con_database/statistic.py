class Statistic:
    def __init__(self, surveys):
        self.__surveys = surveys
        self.__total_participants = len(surveys)
        self.__average_age = self.__compute_average_age()
        self.__average_height = self.__compute_average_height()
        self.__name_counts = self.__compute_name_count()
        self.__subject_counts = self.__compute_subject_count()
        self.__yes_no_counts = self.__compute_yes_no_count()

    def get_total_participants(self):
        return self.__total_participants
    
    def get_average_age(self):
        return self.__average_age
    
    def get_average_height(self):
        return self.__average_height
    
    def get_name_counts(self):
        return self.__name_counts
    
    def get_subject_counts(self):
        return self.__subject_counts
    
    def get_yes_no_counts(self):
        return self.__yes_no_counts

    def __compute_average_age(self):
        ages = []
        for survey in self.__surveys:
            ages.append(survey.get_age())

        return sum(ages) / self.__total_participants
    
    def __compute_average_height(self):
        heights = []
        for survey in self.__surveys:
            heights.append(survey.get_height())

        return sum(heights) / self.__total_participants
    
    def __compute_name_count(self):
        count = {}
        for survey in self.__surveys:
            name = survey.get_name()
            count[name] = count.get(name, 0) + 1

        return count 
    
    def __compute_subject_count(self):
        count = {}
        for survey in self.__surveys:
            subjects = survey.get_subjects() # Lista di materie
            for subject in subjects:
                count[subject] = count.get(subject, 0) + 1

        return count

    def __compute_yes_no_count(self):
        count = {}
        for survey in self.__surveys:
            key = str(survey.get_married())
            count[key] = count.get(key, 0) + 1

        count['True'] = (count.get('True', 0) / self.__total_participants) * 100
        count['False'] = (count.get('False', 0) / self.__total_participants) * 100

        return count