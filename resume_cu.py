import argparse
import os
import sys

# Добавляем путь к GTK в список DLL-директорий Windows (требуется для WeasyPrint)
gtk_path = r"D:\ProgramFiles\GTK3-Runtime Win64\bin"
if os.path.exists(gtk_path) and hasattr(os, 'add_dll_directory'):
    os.add_dll_directory(gtk_path)

try:
    from weasyprint import HTML
except ImportError:
    print("Ошибка: WeasyPrint не установлен. Установите его командой: pip install weasyprint")
    sys.exit(1)

def main():
    # Настройки по умолчанию для версии CU
    input_file = "src/resume_cu.html"
    output_file = "Resume_CU_Long.pdf"
    
    # Проверяем наличие входного файла
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл {input_file} не найден.")
        return

    print(f"Генерация 'длинного' резюме из {input_file}...")
    
    # Рендерим PDF. WeasyPrint подхватит настройки @page из CSS.
    # Для "колбасы" в CSS должно быть прописано size: 210mm auto; или просто ширина.
    HTML(input_file).write_pdf(output_file)
    
    print(f"Успешно! Результат: {os.path.abspath(output_file)}")

if __name__ == '__main__':
    main()
