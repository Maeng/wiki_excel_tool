from enum import Enum
import re


class RegexRefineEnum(Enum):
    CEO = "(display_name|original_title)"
    CAPITAL = '(display_name)'
    PLACE_LOCATED = '(display_name)'
    PRESIDENT_INFO = ''
    POPULATION = '(refined_value)'
    HEIGHT = '(refined_value)'
    HEIGHT_OF_PERSON = '(refined_value)'
    GEOGRAPHICAL_AREA = '(refined_value)'
    DATE_OF_BIRTH = '(date)'
    DATE_OF_DEATH = '(date)'
    RELEASE_DATE = '(date)'
    FILM_DIRECTOR = '(display_name)'
    MUSIC_GROUP_MEMBER = '(display_name)'
    GDP_PPP = ''

    def __init__(self, regex_type):
        self.regex_type = regex_type

    def regex(self, regex_data):
        if self.regex_type == RegexRefineEnum.CEO.value:
            return re.compile(RegexRefineEnum.CEO.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.CAPITAL.value:
            return re.compile(RegexRefineEnum.CAPITAL.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.PLACE_LOCATED.value:
            return re.compile(RegexRefineEnum.PLACE_LOCATED.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.PRESIDENT_INFO.value:
            return re.compile(RegexRefineEnum.PRESIDENT_INFO.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.POPULATION.value:
            return re.compile(RegexRefineEnum.POPULATION.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.HEIGHT.value:
            return re.compile(RegexRefineEnum.HEIGHT.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.HEIGHT_OF_PERSON.value:
            return re.compile(RegexRefineEnum.HEIGHT_OF_PERSON.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.GEOGRAPHICAL_AREA.value:
            return re.compile(RegexRefineEnum.GEOGRAPHICAL_AREA.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.DATE_OF_BIRTH.value:
            return re.compile(RegexRefineEnum.DATE_OF_BIRTH.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.DATE_OF_DEATH.value:
            return re.compile(RegexRefineEnum.DATE_OF_DEATH.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.RELEASE_DATE.value:
            return re.compile(RegexRefineEnum.RELEASE_DATE.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.FILM_DIRECTOR.value:
            return re.compile(RegexRefineEnum.FILM_DIRECTOR.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.MUSIC_GROUP_MEMBER.value:
            return re.compile(RegexRefineEnum.MUSIC_GROUP_MEMBER.value).findall(regex_data)
        elif self.regex_type == RegexRefineEnum.GDP_PPP.value:
            return re.compile(RegexRefineEnum.GDP_PPP.value).findall(regex_data)
