from config import config
from utils import create_database, save_data_to_database, user_interactive

if __name__ == '__main__':
    employers_ids = ['80',     # Альфа-Банк
                     '1740',   # Яндекс
                     '4181',   # ВТБ
                     '4219',   # Tele2
                     '1373',   # "Аэрофлот"
                     '39305',  # Газпром нефть
                     '3388',   # Газпромбанк
                     '15478',  # VK
                     '4233',   # X5 Group
                     '78638'   # Тинькофф
                     ]

    params = config()

    create_database("сoursework5", params)
    save_data_to_database(employers_ids, "сoursework5", params)
    user_interactive("сoursework5")
