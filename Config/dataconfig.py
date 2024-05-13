import os

class TestData:
    """this is base of url"""
    BASE_URL_DEV = "https://feedlot.id"
    BASE_URL_TESTING = "https://accel.id"
    BASE_URL_PROD = "https://portalkerja.co.id"

    """This is General Password"""
    PWD_SUPERADMIN = os.environ.get("PWD_SUPERADMIN")
    PWD_ALL_ROLE = os.environ.get("PWD_ALL_ROLE")
    INVALID_PASSWORD = "JDJ009"
    BLANK_PASSWORD = ""

    """This is all EMAIL Account Test Data"""
    SUPERADMIN_27 = "visiprimaqa+27@gmail.com"
    JOB_SEEKER_ONLY = ""
    JOB_SEEKER_HRMS_ADMIN = ""
    JOB_SEEKER_HRMS_EMPLOYEE = ""

    JOB_POSTER_ADM_ONLY = ""
    JOB_POSTERADM_HRMS_ADM = ""
    JOB_POSTERADM_HRMS_EMPLOYEE = ""



