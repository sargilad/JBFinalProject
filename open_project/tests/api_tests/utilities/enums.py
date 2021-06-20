from enum import Enum


class WorkPackageType(Enum):
    TASK = 'TASK'
    MILESTONE = 'MILESTONE'
    PHASE = 'PHASE'


class SideMenuItems(Enum):
    WORK_PACKAGES = "Work packages"
    ALL_OPEN = "All open"


class WorkPackagesTableHeaders(Enum):
    TYPE = 'TYPE'
    SUBJECT = 'SUBJECT'
