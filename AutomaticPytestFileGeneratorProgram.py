import pathlib
import re

# ディレクトリの基本構成
# (project) の部分は開発する Python プログラムの名前
#
# (project)
# ├── (project)  ............ プログラムのソースコードディレクトリ
# │  ├── __init__.py
# │  └── *.py
# └── tests  ................ 単体テストのソースコードディレクトリ
#    ├── __init__.py
#    └── *.py

_pytest_root_path = "tests\\"
_pytest_first_filename = "\\test_"


def automatic_pytest_file_generator() -> None:
    # target_path = get_standard_input_data()
    target_path = "./sampleproject"
    for target_folder in pathlib.Path(target_path).glob("**"):
        pytest_folder = pathlib.Path(_pytest_root_path + str(target_folder))
        if not pytest_folder.exists():
            pytest_folder.mkdir()
        create_pytest_folder(target_folder)


def get_standard_input_data() -> str:
    """標準入力からテスト対象のパスを取得する"""
    return input("pytest target path = ")


def create_pytest_folder(target_folder: pathlib.Path) -> None:
    """{path}内のフォルダに対して処理をする"""
    for target_file in target_folder.glob("*.py"):
        pytest_file = pathlib.Path(_pytest_root_path + str(target_file))
        if not pytest_file.exists():
            create_pytest_file(target_file)


def create_pytest_file(target_file: pathlib.Path) -> None:
    """{path}内の.pyファイルに対して処理をする"""
    pytest_file = pathlib.Path(
        _pytest_root_path
        + str(target_file.parent)
        + _pytest_first_filename
        + target_file.name
    )
    if not pytest_file.exists():
        write_list = read_pytest_data(target_file)
        # import の設定
        if write_list != list():
            write_list.insert(0, "import pytest, sys, pathlib")
            write_list.insert(1, "if not str(pathlib.Path.cwd()) in sys.path:")
            write_list.insert(2, "    sys.path.append(str(pathlib.Path.cwd()))")
            write_list.insert(
                3,
                "from {} import {}".format(
                    str(target_file.parent).replace("\\", "."), target_file.stem
                ),
            )
        write_pytest_data(pytest_file, write_list)


def read_pytest_data(target_file: pathlib.Path) -> list:
    func_name_list = list()
    with target_file.open(mode="rt", encoding="utf-8") as file_py:
        for r_line in file_py.readlines():
            r_data = r_line.split()
            if len(r_data) > 0 and r_data[0] == "def":
                func_name_list.extend(re.findall("(.*)\(", r_data[1]))
    return func_name_list


def write_pytest_data(pytest_file: pathlib.Path, write_list: list) -> None:
    if write_list != list():
        with pytest_file.open(mode="wt", encoding="utf-8") as w_file:
            w_file.write("{}\n".format(write_list[0]))
            w_file.write("{}\n".format(write_list[1]))
            w_file.write("{}\n".format(write_list[2]))
            w_file.write("{}\n\n".format(write_list[3]))
            for pytest_func in write_list[4:]:
                w_file.write("def test_{}():\n".format(pytest_func))
                w_file.write("    pass\n\n\n")


if __name__ == "__main__":
    print(automatic_pytest_file_generator())
