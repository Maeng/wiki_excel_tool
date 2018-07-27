from enum import Enum
from refine_type.regex_refine_enum import RegexRefineEnum


class AttributeEnum(Enum):
    CEO = 'ceo'
    FILM_DIRECTOR = 'film_director'
    MUSIC_GROUP_MEMBER = 'music_group_member'
    RELEASE_DATE = 'release_date'
    HEIGHT = 'height'
    HEIGHT_OF_PERSON = 'height_of_person'
    GEOGRAPHICAL_AREA = 'geographical_area'
    DATE_OF_DEATH = 'date_of_death'
    DATE_OF_BIRTH = 'date_of_birth'
    GDP_PPP = 'gdp_ppp'
    CAPITAL = 'capital'
    POPULATION = 'population'
    PLACE_LOCATED = 'place_located'
    PRESIDENT_INFO = 'president_info'

    def __init__(self, attribute_en):
        self.attribute_en = attribute_en

    def regex(self, regex_data):
        if self.regex_type == RegexRefineEnum.CEO.value:
            return RegexRefineEnum.CEO.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.CAPITAL.value:
            return RegexRefineEnum.CAPITAL.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.PLACE_LOCATED.value:
            return RegexRefineEnum.PLACE_LOCATED.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.PRESIDENT_INFO.value:
            return RegexRefineEnum.PRESIDENT_INFO.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.POPULATION.value:
            return RegexRefineEnum.POPULATION.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.HEIGHT.value:
            return RegexRefineEnum.HEIGHT.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.HEIGHT_OF_PERSON.value:
            return RegexRefineEnum.HEIGHT_OF_PERSON.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.GEOGRAPHICAL_AREA.value:
            return RegexRefineEnum.GEOGRAPHICAL_AREA.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.DATE_OF_BIRTH.value:
            return RegexRefineEnum.DATE_OF_BIRTH.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.DATE_OF_DEATH.value:
            return RegexRefineEnum.DATE_OF_DEATH.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.RELEASE_DATE.value:
            return RegexRefineEnum.RELEASE_DATE.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.FILM_DIRECTOR.value:
            return RegexRefineEnum.FILM_DIRECTOR.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.MUSIC_GROUP_MEMBER.value:
            return RegexRefineEnum.MUSIC_GROUP_MEMBER.regex(regex_data)
        elif self.regex_type == RegexRefineEnum.GDP_PPP.value:
            return RegexRefineEnum.GDP_PPP.regex(regex_data)
