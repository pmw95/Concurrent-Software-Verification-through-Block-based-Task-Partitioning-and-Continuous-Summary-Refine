import xml.etree.ElementTree as tree
import os

from Run import Run

path = '../CPAchecker/test/results/'

def parse():
    results = {}

    for file in os.listdir(path):
        if file.endswith('.xml'):
            result = tree.parse(path + file).getroot()
            name = result.get('name').split('.')[0]
            if name not in results:
                results[name] = []

            for run in result.iter('run'):
                run_name = run.get('name')
                run_time = run.find(".//*[@title='cputime']").get('value')
                expected = run.get('expectedVerdict')
                status = run.find(".//*[@title='status']").get('value')
                category = run.find(".//*[@title='category']").get('value')

                run = Run(run_name, run_time, expected, status, category)
                results[name].append(run)

    return results
