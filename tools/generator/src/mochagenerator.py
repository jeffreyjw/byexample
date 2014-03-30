from generator import *
import os
import json
import re


class MochaGenerator(Generator):

    def __init__(self):
        self.directory = "{0}..{0}example2".format(os.sep)
        self.command = "grunt"
        self.report_file = "report.json"
        self._path = False
        self._working_path = False
        self.open_tag = "//<"
        self.close_tag = "//>"


    def _go_to_working_dir(self, inside_dir=""):
        path = os.getcwd()

        new_path = path + self.directory

        if inside_dir != "":
            new_path += os.sep + inside_dir

        os.chdir(new_path)
        self._working_path = new_path

        if not self._path:
            self._path = path


    def _revert_dir(self):
        if self._path:
            os.chdir(self._path)
            self._working_path = self._path
            self._path = False


    def get_tags_from_file(self, data, tests):

        tags = []
        is_in_tag = False
        tag = ""
        preg_open = re.compile(r"^\s*"+self.open_tag)
        preg_close = re.compile(r"^\s*"+self.close_tag)
        lines = data.split("\n")

        for line in lines:
            print is_in_tag
            if preg_open.match(line):
                tag = line + "\n"
                is_in_tag = True

            elif preg_close.match(line):
                tags.append(tag)
                is_in_tag = False

            elif is_in_tag:
                tag += line + "\n"

        return tags


    def read_documentation_tags(self, tests):
        self._go_to_working_dir("test{0}spec".format(os.sep))

        all_tags = []

        for root, subFolders, files in os.walk(os.getcwd()):
            for one_file in files:
                f = open(one_file)
                data = f.read()
                f.close()
                tags = self.get_tags_from_file(data, tests)
                all_tags.append(tags)


        self._revert_dir()

        return all_tags


    def read_json_report(self):
        self._go_to_working_dir()
        os.system(self.command)
        f = open(self.report_file, "r")
        data = f.read()
        f.close()

        self._revert_dir()

        return json.loads(data)


    def report(self):
        data = self.read_json_report()
        all_tags = self.read_documentation_tags(data["tests"])

        data["documentation"] = all_tags

        return data