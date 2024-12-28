import argparse
from weasyprint import HTML


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description='Convert HTML to PDF.')
    parser.add_argument('-inp', '--input_file', type=str, default="src/resume.html",
                        help='Path to the input HTML file.')
    parser.add_argument('-out', '--output_file', type=str, default="CV0.pdf", help='Path to the output PDF file.')

    # Парсим аргументы
    args = parser.parse_args()

    # Используем WeasyPrint для конвертации
    HTML(args.input_file).write_pdf(args.output_file, options={
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0'
    })


if __name__ == '__main__':
    main()
