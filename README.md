Тестове задание

1. Выполнена основная часть. Доп часть, сделаю самостоятельно: освою новую фишку.
2. Все числовые значения округлены до 2х знаков после точки.
3. Для настройки регулярного получения api использован пакет APScheduler
   Запуск сервера осуществляется командой python3 manage.py runserver --noreload
   Чтобы избежать запуска двух воркеров.
4. Задание реализовано с помощью двух таблиц в БД:
    Основная - для записи текущих значени индекса
    Дополнительная - для обработки расчетов по кастомному периоду
5. Для обработки расчетов создан дополнительный контроллер
6. В решении использован один html шаблон и два url маршрута.
7. Форма разбита на дату и время отдельно.
