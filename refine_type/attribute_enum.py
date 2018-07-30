from enum import Enum


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
