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


    def find_test_name(self, code, tests):

        for test in tests:
            if code.find(test["title"]) != -1:
                return test["title"]
        return ""


    def get_tags_from_file(self, data, tests):

        tags = []
        is_in_tag = False
        tag = ""
        tag_line_number = 0
        tag_head = False
        preg_open = re.compile(r"^\s*"+self.open_tag)
        preg_close = re.compile(r"^\s*"+self.close_tag)
        lines = data.split("\n")
        article_titles = []

        line_number = 1

        for line in lines:
            if preg_open.match(line):
                tag = ""
                is_in_tag = True
                tag_head = True
                article_titles = []

            elif preg_close.match(line):
                name = self.find_test_name(tag, tests)
                tags.append({"title": name, "code": tag, "line": tag_line_number, "articles": article_titles})
                is_in_tag = False

            elif is_in_tag:
                tag += line + "\n"

            if tag_head:
                tag_line_number = line_number + 1

                article_pos = line.find("@article")
                if article_pos != -1:
                    article_title = line[article_pos+8:].strip()
                    article_titles.append(article_title)
                else:
                    tag_head = False

            line_number += 1

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


    def documentation_test_status(self, data):

        for test_file in data["documentation"]:
            for test in test_file:
                for test_passed in data["passes"]:
                    if test["title"] == test_passed["title"]:
                        test["status"] = "passed"

                for test_failed in data["failures"]:
                    if test["title"] == test_failed["title"]:
                        test["status"] = "failed"

        return data


    def generate_articles(self, data):
        test_files = data["documentation"]
        articles = {}

        for test_file in test_files:
            for test in test_file:
                for article in test["articles"]:
                    if article not in articles:
                        articles[article] = []

                    articles[article].append(test)

        data["documentation"] = articles


        return data


    def report(self):
        data = self.read_json_report()
        all_tags = self.read_documentation_tags(data["tests"])

        data["documentation"] = all_tags

        data = self.documentation_test_status(data)
        data = self.generate_articles(data)

        return data