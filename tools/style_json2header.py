from io import TextIOWrapper
import sys
import datetime
import json

class JSONManager:

    def __init__(self, filepath : str) -> None:
        self.filepath : str = filepath
        self.file : TextIOWrapper = open(self.filepath, "r")

        self.json = json.load(self.file)

    def get_json(self):
        return self.json

    def close(self) -> None:
        self.file.close()

class HeaderManager:

    def __init__(self, filepath : str, json_contents) -> None:
        self.filepath = filepath
        self.json_data = json_contents

        self.date : list[int] = [datetime.datetime.now().date().year, datetime.datetime.now().date().month, datetime.datetime.now().date().day]
        self.time : list[int] = [datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second, datetime.datetime.now().time().microsecond]
        
        self.header : str = \
            f'/* Generated on {self.date[1]}/{self.date[2]}/{self.date[0]}. {self.time[0]}:{self.time[1]}:{self.time[2]}:{self.time[3]} */\n' + \
            f'#ifndef {self.json_data["name"]}_STYLE_MZUI_H\n' + \
            f'#define {self.json_data["name"]}_STYLE_MZUI_H\n' + \
            '#include <MuzzleUI.h>\n' + \
            '\n\n\n'
        self.contents : str = None
        self.footer : str = \
            f'#endif // {self.json_data["name"]}_STYLE_MZUI_H'

        self.date : list[int] = [datetime.datetime.now().date().year, datetime.datetime.now().date().month, datetime.datetime.now().date().day]
        self.time : list[int] = [datetime.datetime.now().time().hour, datetime.datetime.now().time().minute, datetime.datetime.now().time().second, datetime.datetime.now().time().microsecond]


        self.output = open(self.filepath, "w")

    def prepare(self) -> None:
        pressed = self.json_data["style"]["rectangle"]["pressed"]
        hover = self.json_data["style"]["rectangle"]["hover"]
        disabled = self.json_data["style"]["rectangle"]["disabled"]
        regular = self.json_data["style"]["rectangle"]["regular"]

        self.contents = \
            f'MuzzleUI_Style {self.json_data["name"]}_gen_struct()\n' + \
            '{\n' + \
            '\tMuzzleUI_Style buf;\n' + \
            '\tbuf.rectangle.pressed.color.r = ' + f'{pressed["color"]["r"]};\n' + \
            '\tbuf.rectangle.pressed.color.g = ' + f'{pressed["color"]["g"]};\n' + \
            '\tbuf.rectangle.pressed.color.b = ' + f'{pressed["color"]["b"]};\n' + \
            '\tbuf.rectangle.pressed.color.a = ' + f'{pressed["color"]["a"]};\n' + \
            '\tbuf.rectangle.pressed.border.use = ' + f'{pressed["border"]["use"]};\n' + \
            '\tbuf.rectangle.pressed.border.size = ' + f'{pressed["border"]["size"]};\n' + \
            '\tbuf.rectangle.pressed.border.color.r = ' + f'{pressed["border"]["color"]["r"]};\n' + \
            '\tbuf.rectangle.pressed.border.color.g = ' + f'{pressed["border"]["color"]["g"]};\n' + \
            '\tbuf.rectangle.pressed.border.color.b = ' + f'{pressed["border"]["color"]["b"]};\n' + \
            '\tbuf.rectangle.pressed.border.color.a = ' + f'{pressed["border"]["color"]["a"]};\n' + \
            '' + \
            '\tbuf.rectangle.hover.color.r = ' + f'{hover["color"]["r"]};\n' + \
            '\tbuf.rectangle.hover.color.g = ' + f'{hover["color"]["g"]};\n' + \
            '\tbuf.rectangle.hover.color.b = ' + f'{hover["color"]["b"]};\n' + \
            '\tbuf.rectangle.hover.color.a = ' + f'{hover["color"]["a"]};\n' + \
            '\tbuf.rectangle.hover.border.use = ' + f'{hover["border"]["use"]};\n' + \
            '\tbuf.rectangle.hover.border.size = ' + f'{hover["border"]["size"]};\n' + \
            '\tbuf.rectangle.hover.border.color.r = ' + f'{hover["border"]["color"]["r"]};\n' + \
            '\tbuf.rectangle.hover.border.color.g = ' + f'{hover["border"]["color"]["g"]};\n' + \
            '\tbuf.rectangle.hover.border.color.b = ' + f'{hover["border"]["color"]["b"]};\n' + \
            '\tbuf.rectangle.hover.border.color.a = ' + f'{hover["border"]["color"]["a"]};\n' + \
            '' + \
            '\tbuf.rectangle.disabled.color.r = ' + f'{disabled["color"]["r"]};\n' + \
            '\tbuf.rectangle.disabled.color.g = ' + f'{disabled["color"]["g"]};\n' + \
            '\tbuf.rectangle.disabled.color.b = ' + f'{disabled["color"]["b"]};\n' + \
            '\tbuf.rectangle.disabled.color.a = ' + f'{disabled["color"]["a"]};\n' + \
            '\tbuf.rectangle.disabled.border.use = ' + f'{disabled["border"]["use"]};\n' + \
            '\tbuf.rectangle.disabled.border.size = ' + f'{disabled["border"]["size"]};\n' + \
            '\tbuf.rectangle.disabled.border.color.r = ' + f'{disabled["border"]["color"]["r"]};\n' + \
            '\tbuf.rectangle.disabled.border.color.g = ' + f'{disabled["border"]["color"]["g"]};\n' + \
            '\tbuf.rectangle.disabled.border.color.b = ' + f'{disabled["border"]["color"]["b"]};\n' + \
            '\tbuf.rectangle.disabled.border.color.a = ' + f'{disabled["border"]["color"]["a"]};\n' + \
            '' + \
            '\tbuf.rectangle.regular.color.r = ' + f'{regular["color"]["r"]};\n' + \
            '\tbuf.rectangle.regular.color.g = ' + f'{regular["color"]["g"]};\n' + \
            '\tbuf.rectangle.regular.color.b = ' + f'{regular["color"]["b"]};\n' + \
            '\tbuf.rectangle.regular.color.a = ' + f'{regular["color"]["a"]};\n' + \
            '\tbuf.rectangle.regular.border.use = ' + f'{regular["border"]["use"]};\n' + \
            '\tbuf.rectangle.regular.border.size = ' + f'{regular["border"]["size"]};\n' + \
            '\tbuf.rectangle.regular.color.r = ' + f'{regular["border"]["color"]["r"]};\n' + \
            '\tbuf.rectangle.regular.color.g = ' + f'{regular["border"]["color"]["g"]};\n' + \
            '\tbuf.rectangle.regular.color.b = ' + f'{regular["border"]["color"]["b"]};\n' + \
            '\tbuf.rectangle.regular.color.a = ' + f'{regular["border"]["color"]["a"]};\n' + \
            '\n\treturn buf;\n' + \
            '}\n\n'
    def write(self) -> None:
        self.output.write(f"{self.header}{self.contents}{self.footer}")

    def close(self) -> None:
        self.output.close()


def main() -> None :
    filepath : str = sys.argv[1]
    print(f"Style: {filepath}")
    output : str = sys.argv[2]
    print(f"Output: {output}")

    StyleJSON = JSONManager(filepath)

    print(f'Generating {StyleJSON.get_json()["name"]}')
    json_contents : str = StyleJSON.get_json()

    Header = HeaderManager(output, json_contents)

    Header.prepare()
    Header.write()

    StyleJSON.close()
    Header.close()

main()
