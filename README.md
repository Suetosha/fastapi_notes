### Для запуска приложения:

1. Создать env файл со следующими переменными: \
DB_HOST=db \
DB_PORT=5432 \
DB_NAME=fastapi_notes \
DB_USER=postgres \
DB_PASS=123 \
SECRET=abc 
2. Выполнить docker compose up из корня проекта 
3. Для тестирования в Postman добавить переменные: 
* base_url, current_value = http://127.0.0.1:8000
* access_token, поле оставить пустым
