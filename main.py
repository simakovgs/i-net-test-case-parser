import sys
from textfsm import TextFSM


def parse(template_file, input_file):
    try:
        with open(template_file) as f_template, open(input_file) as f_input:
            fsm = TextFSM(f_template)
            input_data = f_input.read()

            result = fsm.ParseText(input_data)

            for entry in result:
                for name, value in zip(fsm.header, entry):
                    if name in ['DEVICE_NAME', 'STATE']:
                        print(f'{name}: "{value}"')
                    else:
                        print(f'{name}: {value}')


    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python textfsm_parser.py <input_file>")
        sys.exit(1)
    parse('template.textfsm', sys.argv[1])