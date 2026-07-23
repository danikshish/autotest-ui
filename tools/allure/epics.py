from enum import Enum

class AllureEpic(str, Enum):
    LMS = 'LMS system'
    STUDENT = 'Studeent system'
    ADMINISTRATION = 'Administration system'