import argparse
import os
import sys

# Добавляем путь к GTK в список DLL-директорий Windows (требуется для Python 3.8+)
gtk_path = r"D:\ProgramFiles\GTK3-Runtime Win64\bin"
if os.path.exists(gtk_path) and hasattr(os, 'add_dll_directory'):
    os.add_dll_directory(gtk_path)

from weasyprint import HTML

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description='Convert HTML to PDF.')
    parser.add_argument('-inp', '--input_file', type=str, default="src/resume_cu.html",
                        help='Path to the input HTML file.')
    parser.add_argument('-out', '--output_file', type=str, default="CV_Dulina_Irina.pdf", help='Path to the output PDF file.')

    # Парсим аргументы
    args = parser.parse_args()

    # Используем WeasyPrint для конвертации
    HTML(args.input_file).write_pdf(args.output_file, options={
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'page-size': 'A4',  # Указание размера страницы
    })

if __name__ == '__main__':
    main()
