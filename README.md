# Mini_project_shop
1. Создание виртуального окружения
Создайте и активируйте виртуальное окружение для управления зависимостями.

python -m venv venv
source venv/bin/activate

python example.py

 Объяснение функциональности: Классы и их роли:  Product: Описывает товар с атрибутами name и price. Дандер-методы __eq__ и __lt__ позволяют сравнивать товары по цене. Customer: Управляет заказами клиента и подсчитывает общую сумму всех заказов. Order: Учитывает заказы, отслеживает общее количество и стоимость всех заказов. Discount: Обрабатывает скидки через статические методы для различных сценариев. Функции скидок:  Сезонная скидка: Фиксированная скидка 10%. Промокод: Пользовательская скидка в процентах. Вывод данных:  Для каждого клиента отображается информация о заказах и их общей стоимости. Печатается общая статистика по количеству и сумме всех заказов. Этот код демонстрирует основные аспекты работы с объектно-ориентированным программированием и учитывает все требования, указанные в задании.
