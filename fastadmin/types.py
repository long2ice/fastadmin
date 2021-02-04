from enum import Enum


class Order(str, Enum):
    ASC = "ASC"
    DESC = "DESC"
