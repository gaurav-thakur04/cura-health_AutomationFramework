from SeleniumFrameWork.base.BasePage import BaseClass

import SeleniumFrameWork.utilities.CustomLogger as cl

class AppointmentForm(BaseClass, ):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # locators values in Appointment form

    _facilityDropdown = "facility" #name
    _facilityTokyo = "Tokyo CURA Healthcare Center"  #value "select tag"
    _facilityHongkong = "Hongkong CURA Healthcare Center"  #value "select tag"
    _facilitySeoul = "Seoul CURA Healthcare Center"  #value "select tag"
    _checkboxHospitalreadmission = "checkbox-inline"  #class
    _healthcareProgMedicare = "radio_program_medicare"  #id
    _healthcareProgMedicaid = "radio_program_medicaid"  # id
    _healthcareProgNone = "radio_program_none"  #id
    _visitDateCalender = None
    _commentBox ="txt_comment"  #id
    _bookAppointmentButton = "btn-book-appointment"   #id

    def clickOnTokyoFacility(self):
        self.dropDown(self._facilityDropdown,"name",self._facilityTokyo)

    def clickOnHongkongFacility(self):
        self.dropDown(self._facilityDropdown, "name", self._facilityHongkong)

    def clickOnSeoulFacility(self):
        self.dropDown(self._facilityDropdown, "name", self._facilitySeoul)

    def clickHospitalReadmission(self):
        self.clickOnElement(self._checkboxHospitalreadmission,"class")

    def clickOnMedicare(self):
        self.clickOnElement(self._healthcareProgMedicare,"id")

    def clickOnMedicaid(self):
        self.clickOnElement(self._healthcareProgMedicaid, "id")

    def clickOnNone(self):
        self.clickOnElement(self._healthcareProgNone, "id")


    def submitButton(self):
        self.clickOnElement(self._bookAppointmentButton, "id")
