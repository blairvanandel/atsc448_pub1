from ruamel import yaml
import pprint
yaml_file=yaml.YAML(typ='safe')
with open('macos_fiona2.yaml','r') as f:
    test=yaml_file.load(f)
    pprint.pprint(test)
    




