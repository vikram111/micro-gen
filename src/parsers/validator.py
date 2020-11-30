import yaml


def validate_spec(spec):
    spec_loaded = yaml.load(spec)
    return spec_loaded
