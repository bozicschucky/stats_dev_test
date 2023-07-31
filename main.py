from app.file_handler import read_json_file
from app.file_handler import write_json_file
from app.file_processor import RecipeAnalyzer


def main():
    file_location = input(
        "Enter location to the file or Press Enter to use the default")
    if file_location:
        data = read_json_file(file_location)
    else:
        data = read_json_file('data.json')

    analyzer = RecipeAnalyzer(data)
    analyzer.analyze()

    # output data ...
    output = analyzer.get_output()
    write_json_file("./output.json", output)


if __name__ == "__main__":
    main()
