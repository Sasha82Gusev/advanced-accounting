from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from lscom import lscom


def print_hi(name):

    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('PyCharm')
    print(datetime.now())
    print('Активные COM порты',lscom.list_active_serial_port_names()) #paket lscom(показывает подключенные COM порты на компьютере)
    calculate_salary()
    get_employees()