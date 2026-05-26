import os
import re
import ollama

MODEL_NAME = "llama3"

def generate_dq_tests(sql_file_path: str):
    try:
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()

        print(f"[*] Анализирую структуру таблицы из {sql_file_path}...")

        system_prompt = (
            "Ты - инженер по качеству данных (Data Quality Engineer). "
            "На основе SQL-кода таблицы создай YAML файл с тестами dbt. "
            "Для каждой колонки предложи базовые тесты (not_null, unique) "
            "и логические тесты (accepted_values, positive_values)."
            "Отвечай только чистым YAML кодом."
        )

        response = ollama.generate(
            model=MODEL_NAME,
            system=system_prompt,
            prompt=f"Сгенерируй YAML тесты для этого SQL: {sql_content}"
        )

        yaml_content = response['response'].replace('```yaml', '').replace('```', '').strip()

        output_path = "schema_tests.yml"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(yaml_content)

        print(f"[+] Файл тестов качества данных создан: {output_path}")

    except Exception as e:
        print(f"[!] Ошибка: {e}")

if __name__ == "__main__":
    path = input("Введите путь к SQL файлу: ")
    generate_dq_tests(path)