
from app.helpers.file_handler import read_json_file;
from app.helpers.file_handler import write_json_file;


def main():
  data = read_json_file('data.json')
  print("main function....", data);
  write_json_file("./output.json" , {"user2":"2"});

if __name__ == "__main__":
    main()