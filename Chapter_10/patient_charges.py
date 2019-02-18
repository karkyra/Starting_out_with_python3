from patient import *
from procedure import *

def main():

    patient_info = Patient('James','Jon' ,'Smith', 'Atlanta', 'Georgia', '60194', '222-444-4545', 'Marry Cordova', '222-444-5555')


    print("Patient Information")
    print("___________________")
    print("First name: ", patient_info.get_f_name(), "\nMiddle Name: ", patient_info.get_m_name(), "\nLast Name: ", patient_info.get_l_name())
    print()
    print("Patiet Address")
    print("---------------")
    print("City: ", patient_info.get_city(), "\nState: ", patient_info.get_state(), "\nZip Code: ", patient_info.get_zip_code(), \
          "\nPhone Number: ", patient_info.get_p_number() , "\nEmergency contact: ", patient_info.get_e_name(), "\nEmergency concact phone: ", patient_info.get_e_phone())


    prod_1 = Procedure("Physical Exam", "02/16/2019", "dr. Irvine", float(250.00))
    prod_2 = Procedure("X-Ray", "02/16/2019", "dr. Jamison", float(500.00))
    prod_3 = Procedure("Blood test", "02/16/2019", "dr. Smith", float(200.00))

    print()
    print("Procedure #1")
    print("=============")
    print("Procedure name: ", prod_1.get_prod_name(), "\nDate: ", prod_1.get_prod_date(), "\nPractitioner: ", prod_1.get_practitioner(),"\nCharge", prod_1.get_charge())

    print("Procedure #2")
    print("=============")
    print("Procedure name: ", prod_2.get_prod_name(), "\nDate: ", prod_2.get_prod_date(), "\nPractitioner: ", prod_2.get_practitioner(),"\nCharge", prod_2.get_charge())

    print("Procedure #3")
    print("=============")
    print("Procedure name: ", prod_3.get_prod_name(), "\nDate: ", prod_3.get_prod_date(), "\nPractitioner: ", prod_3.get_practitioner(),"\nCharge", prod_3.get_charge())

    print()
    print("==============")
    total = prod_1.get_charge() + prod_2.get_charge() + prod_3.get_charge()
    print("Total charges:", total )

main()
