#!/usr/bin/env python
import os
import sys

def main():
    """Запускает административные задачи Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tattoo_site.settings')  # Указываем путь к настройкам Django

    from django.core.management import execute_from_command_line  # Импортируем команду для выполнения
    execute_from_command_line(sys.argv)  # Выполняем команду, переданную в аргументах командной строки

if __name__ == '__main__':
    main()  # Вызываем функцию для запуска команд Django
