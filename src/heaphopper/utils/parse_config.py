import yaml

def parse_config(config_file):
    config = yaml.load(config_file)
    if 'global_config' in config:
        with open(config['global_config']) as f:
            base = yaml.load(f)
            for k, v in base.iteritems():
                if k not in config:
                    config[k] = v
    # Insert parsing here if necessary
    return config
