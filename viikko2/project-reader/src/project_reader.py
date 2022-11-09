import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        tomli_dict = tomli.loads(content)
        name = tomli_dict["tool"]["poetry"]["name"]
        desc = tomli_dict["tool"]["poetry"]["description"]
        dependencies = tomli_dict["tool"]["poetry"]["dependencies"].keys()
        dev_deps = tomli_dict["tool"]["poetry"]["dev-dependencies"].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_deps)
