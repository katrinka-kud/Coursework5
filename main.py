from config import EMPLOYERS_URL
from classes import Employer, Vacancy

if __name__ == '__main__':
    hh_key = EMPLOYERS_URL
    employers_ids = ['80',  # Альфа-Банк
                     '1740',  # Яндекс
                     '4181',  # ВТБ
                     '4219',  # Tele2
                     '1373',  # "Аэрофлот"
                     '39305',  # Газпром нефть
                     '3388',  # Газпромбанк
                     '15478',  # VK
                     '4233',  # X5 Group
                     '78638'  # Тинькофф
                     ]

    employers_list = Employer.initiate_from_hh(employers_ids)
    print(employers_list[9].employer_name)

    vacancies_list = Vacancy.initiate_from_hh(employers_list[9].employer_id)
    for x in vacancies_list:
        print(x.currency)
