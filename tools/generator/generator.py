from tools.generator.src.mochagenerator import *
import json


def main():
    generator = MochaGenerator()
    report = generator.report()

    json_str = json.dumps(report)

    f = open("documentation.json", "w")
    f.write(json_str)
    f.close()

    return

if __name__ == "__main__":
    main()
