import enum


class args_class:
    class ErroeCode(enum.Enum):
        OK = enum.auto()
        MISSING_STRING = enum.auto()
        MISSING_INTEGER = enum.auto()
        INVALID_INTEGER = enum.auto()
        UNEXPECTED_ARGUMENT = enum.auto()

    def __init__(self, schema, *args) -> None:
        self.unexpectedArguments = set()
        self.boolean_args = dict()
        self.string_args = dict()
        self.int_args = dict()
        self.args_found = set()
        self.current_argument = 0
        self.error_argument_id = "\0"
        self.error_parameter = "TILT"
        self.error_code = self.ErroeCode.OK

        self.schema = schema
        self.args = [arg for arg in args]
        self.valid = self.parse()
        if self.valid != True:
            raise self.args_exception

    def parse(self) -> bool:
        if len(self.schema) == 0 and len(self.args) == 0:
            return True
        self.parse_schema()
        try:
            self.parse_arguments()
        except self.args_exception as e:
            pass
        return self.valid

    def parse_schema(self) -> bool:
        for element in self.schema.split(","):
            if len(element) > 0:
                trimmed_element = element.strip()
                self.parse_schema_element(trimmed_element)
        return True

    def parse_schema_element(self, element: str) -> None:
        element_id = element[0]
        element_tail = element[1:]
        self.validate_schema_element_id(element_id)
        if self.is_boolean_schema_element(element_tail):
            self.parse_boolean_schema_element(element_id)
        elif self.is_string_schema_element(element_tail):
            self.parse_string_schema_element(element_id)
        elif self.is_integer_schema_element(element_tail):
            self.parse_integer_schema_element(element_id)
        else:
            raise ValueError("引数: {} の書式が不正です: {}.".format(element_id, element_tail), 0)

    def validate_schema_element_id(self, element_id: str) -> None:
        if not element_id.isalpha():
            raise ValueError(
                "不正な文字： {} が、次の書式に含まれています： {}".format(element_id, self.schema), 0
            )

    def parse_boolean_schema_element(self, element_id: str) -> None:
        self.boolean_args[element_id] = False

    def parse_integer_schema_element(self, element_id: str) -> None:
        self.int_args[element_id] = 0

    def parse_string_schema_element(self, element_id: str) -> None:
        self.boolean_args[element_id] = ""

    def is_string_schema_element(self, element_tail: str) -> bool:
        return element_tail == "*"

    def is_boolean_schema_element(self, element_tail: str) -> bool:
        return len(element_tail) == 0

    def is_integer_schema_element(self, element_tail: str) -> bool:
        return element_tail == "# "

    def parse_arguments(self) -> bool:
        for self.current_argument in range(len(self.args)):
            arg = self.args[self.current_argument]
            self.parse_argument(arg)
        return True

    def parse_argument(self, arg: str) -> None:
        if arg.startswith("-"):
            self.parse_elements(arg)

    def parse_elements(self, arg: str) -> None:
        for i in range(1, len(arg)):
            self.parse_element(arg[i])

    def parse_element(self, arg_char: str) -> None:
        if self.set_argument(arg_char):
            self.args_found.add(arg_char)
        else:
            self.unexpectedArguments.add(arg_char)
            self.error_code = self.ErroeCode.UNEXPECTED_ARGUMENT
            self.valid = False

    def set_argument(self, arg_char: str) -> bool:
        if self.is_boolean_arg(arg_char):
            self.set_boolean_arg(arg_char, True)
        elif self.is_string_arg(arg_char):
            self.set_string_arg(arg_char)
        elif self.is_int_arg(arg_char):
            self.set_int_arg(arg_char)
        else:
            return False
        return True

    def is_int_arg(self, arg_char: str) -> bool:
        return arg_char in self.int_args.keys()

    def set_int_arg(self, arg_char: str) -> None:
        self.current_argument += 1
        parameter = None
        try:
            parameter = self.args[self.current_argument]
            self.int_args[arg_char] = int(parameter)
        except IndexError as e:
            self.valid = False
            self.error_argument_id = arg_char
            self.error_code = self.ErroeCode.MISSING_INTEGER
            raise self.args_exception()
        except TypeError as e:
            self.valid = False
            self.error_argument_id = arg_char
            self.error_parameter = parameter
            self.error_code = self.ErroeCode.INVALID_INTEGER
            raise self.args_exception()

    def set_string_arg(self, arg_char: str) -> None:
        self.current_argument += 1
        try:
            self.string_args[arg_char] = self.args[self.current_argument]
        except IndexError as e:
            self.valid = False
            self.error_argument_id = arg_char
            self.error_code = self.ErroeCode.MISSING_STRING
            raise self.args_exception()

    def is_string_arg(self, arg_char: str) -> bool:
        return arg_char in self.string_args.keys()

    def set_boolean_arg(self, arg_char: str, value: bool) -> None:
        self.boolean_args[arg_char] = value

    def is_boolean_arg(self, arg_char: str) -> bool:
        return arg_char in self.boolean_args.keys()

    def cardinality(self) -> int:
        return len(self.args_found)

    def usage(self) -> str:
        if len(self.schema) > 0:
            return "[" + self.schema + "]"
        else:
            return ""

    def error_message(self) -> str:
        if self.error_code == self.ErroeCode.OK:
            raise Exception("TILT: ここは実行されないはずです。")
        elif self.error_code == self.ErroeCode.UNEXPECTED_ARGUMENT:
            return self.unexpected_argument_message()
        elif self.error_code == self.ErroeCode.MISSING_STRING:
            return "次の引数のため文字列引数が見つかりません -{}。".format(self.error_argument_id)
        elif self.error_code == self.ErroeCode.INVALID_INTEGER:
            return "引数 -{} には整数が指定されるべきですが、{} が指定されました。".format(
                self.error_argument_id, self.error_parameter
            )
        elif self.error_code == self.ErroeCode.MISSING_INTEGER:
            return "次のパラメータの整数引数が見つかりません {}。".format(self.error_argument_id)
        return ""

    def unexpected_argument_message(self) -> str:
        message = "引数 -"
        for char in self.unexpectedArguments:
            message += char
        message += " は、想定外です。"
        return message

    def false_if_null(self, bl: bool) -> bool:
        return bl != None and bl

    def zero_if_null(self, it: int) -> int:
        return it if it != None else 0

    def blank_if_null(self, st: str) -> str:
        return st if st != None else ""

    def get_string(self, arg_char: str) -> str:
        return self.blank_if_null(self.string_args[arg_char])

    def get_int(self, arg_char: str) -> int:
        return self.zero_if_null(self.int_args[arg_char])

    def get_boolean(self, arg_char: str) -> bool:
        return self.false_if_null(self.boolean_args[arg_char])

    def has(self, arg_char: str) -> bool:
        return arg_char in self.args_found

    def is_valid(self) -> bool:
        return self.valid

    class args_exception(Exception):
        pass
