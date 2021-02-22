from typing import Pattern


class args_class:
    schema = ""
    args = list()
    valid = True
    unexpectedArguments = set()
    boolean_args = dict()
    string_args = dict()
    int_args = dict()
    args_found = dict()
    current_argument = 0
    error_argument_id = "\0"
    error_parameter = "TILT"
    error_code = Exception().__eq__

    def args_class(self, schema, *args) -> None:
        self.schema = schema
        self.args = args
        self.valid = self.parse()
        if self.valid != True:
            raise Exception

    def parse(self) -> bool:
        if len(self.schema) == 0 and len(self.args) == 0:
            return True
        self.parse_schema()
        try:
            parse_arguments()
        except Exception as e:
            pass
        return self.valid

    def parse_schema(self) -> bool:
        for element in self.schema.split(","):
            if len(element) > 0:
                trimmed_element = element.replace(" ", "")
                self.parse_schema_element(trimmed_element)
        return True

    def parse_schema_element(self, element) -> None:
        element_id = element[0]
        element_tail = element[-1]
        self.validate_schema_element_id(element_id)
        if self.is_boolean_schema_element(element_tail):
            self.parse_boolean_schema_element(element_id)
        elif self.is_string_schema_element(element_tail):
            self.parse_string_schema_element(element_id)
        elif self.is_integer_schema_element(element_tail):
            self.parse_integer_schema_element(element_id)
        else:
            raise Exception("引数: {} の書式が不正です: {}.".format(element_id, element_tail))

