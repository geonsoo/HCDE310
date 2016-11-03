class Surveyor():
    """Contains data for one surveyor, with instance variables:
      name-- a string, representing the surveyor's name
      surveys-- a list, containing instances of Survey"""
    def __init__(self, surveyorName, surveys):
        self.name = surveyorName # a string
        self.surveys = surveys # a list of Survey objects

    def survey_count(self):
        return len(self.surveys)

    def maxAge(self):
        if len(self.surveys) == 0: return None
        max_so_far = 0
        for survey in self.surveys:
            for age in survey.ages:
                if age > max_so_far:
                    max_so_far = age
        return max_so_far
        
# alternative implementation using list comprehensions
#        if self.surveys and len(self.surveys) > 0:
#            return max([survey.maxAge() for survey in self.surveys])
#        else:
#            return 0

    def __cmp__(self, other):
        print "comparing", self.name, "and", other.name
        return len(self.surveys) - len(other.surveys)

    def cmp2(self, other):
        if len(self.surveys) > len(other.surveys):
            return 1
        elif len(self.surveys) < len(other.surveys):
            return -1
        else:
            return 0


class Survey():
    "Contains data for one survey"
    def __init__(self, respName, inc, gender, ages, responses):
        self.respondent = respName # a string
        self.income = inc  # a numeric value for household income
        self.gender = gender # 'm' or 'f'
        self.ages = ages  # a list of ages
        self.responses = responses # a list of values; each is 1-5

    def __str__(self):
        s = ''
        s+= "\tRespondent: " + self.respondent + "\n"
        s+= "\tIncome: $%d\n" %  self.income
        s+= "\tGender: " + self.gender + "\n"
        s+= "\tAges of household members: "
        for x in self.ages:
            s+= str(x) + " "
        s += "\n"
        s += "\tResponses: "
        for x in self.responses:
            s+= str(x) + " "
        s += "\n"
        return s

    def maxAge(self):
        if self.ages and len(self.ages)>0:
            return max(self.ages)
        else:
            return None

def populate():
    """creates a dictionary with names as keys and Surveyor instances as vals"""
    # keys will be surveyor names;
    # values will be instances of class Surveyor
    surveyors = {}
    surveyors['Leslie'] = Surveyor('Leslie Knope', [])
    surveyors['Ben'] = Surveyor('Ben Wyatt', [])
    surveyors['Ron'] = Surveyor("Ron Swanson", [])
    surveyors['April'] = Surveyor('April Ludgate', [])

    s = Survey('Sally Citizen', 60000, 'f', [50, 48, 17, 13, 11], [3, 1, 1, 5, 5])
    surveyors['Leslie'].surveys.append(s)
    s = Survey('Norman Neighbor', 40000, 'm', [70, 63], [5, 3, 1, 5, 1])
    surveyors['Leslie'].surveys.append(s)
    s = Survey('Fidel Friend', 62000, 'm', [22], [5, 5, 1, 1, 1])
    surveyors['Ben'].surveys.append(s)
    s = Survey('Earnest Enemy', 18000, 'm', [25], [1, 1, 1, 1, 1])
    surveyors['Ben'].surveys.append(s)
    s = Survey('Harry Helpful', 45000, 'm', [34, 35, 3, 1], [5, 5, 5, 5, 5])
    surveyors['Ben'].surveys.append(s)
    return surveyors

def main():
    surveyors = populate()
    for surveyor in surveyors.values():
        # process each surveyor
        print "Surveys taken by: " + surveyor.name
        for survey in surveyor.surveys:
            # process each survey;
            print survey  # calls the __str__ method on the instance
    
    surveyorList = surveyors.values()
    print "= sort by number of surveys = "
    # this code will use __cmp__for Surveyor() by default
    for s in sorted(surveyorList, reverse=True):
        print "%d surveys completed by %s"%(s.survey_count(), s.name)
    # alternatively, we could have used a lambda function and key
    #for s in sorted(surveyorList, key = lambda s: s.survey_count(), reverse=True):    
    #    print "%d surveys completed by %s"%(s.survey_count(), s.name)
    
    print "= sort by maxAge ="
    # write this yourself, or in class!
    for s in sorted(surveyorList, key = lambda s: s.maxAge(), reverse=True): 
        if s.maxAge() == None:
            print "%s didn't interview anyone!" % s.name
        else: 
            print "%s interviews someone who is %s years old"%(s.name, s.maxAge())
    

if (__name__ == '__main__'):
    main()