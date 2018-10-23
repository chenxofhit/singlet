# vim: fdm=indent
# author:     Fabio Zanini
# date:       02/08/17
# content:    Support module for filenames related to the Google Sheet APIs.
# Modules
import os
import yaml


def _normalize_count_table(sheet):
    if ('format' not in sheet) and ('path' in sheet):
        path = sheet['path']
        if isinstance(path, str):
            fmt = path.split('.')[-1].lower()
        else:
            fmt = [p.split('.')[-1].lower() for p in path]
        sheet['format'] = fmt
    return sheet


def _normalize_samplesheet(sheet):
    if ('format' not in sheet) and ('path' in sheet):
        path = sheet['path']
        sheet['format'] = path.split('.')[-1].lower()

    elif ('google_id' not in sheet) and ('url' in sheet):
        url = sheet['url']
        sheet['google_id'] = url.split('/')[-1]
    return sheet


def _normalize_featuresheet(sheet):
    if ('format' not in sheet) and ('path' in sheet):
        path = sheet['path']
        sheet['format'] = path.split('.')[-1].lower()
    return sheet


def _normalize_dataset(dataset):
    if ('format' not in dataset) and ('path' in dataset):
        path = dataset['path']
        dataset['format'] = path.split('.')[-1].lower()
    return dataset


def reload_config():
    '''Reload the YAML configuration for singlet'''
    config_filename = os.getenv(
            'SINGLET_CONFIG_FILENAME',
            os.getenv('HOME') + '/.singlet/config.yml')
    try:
        with open(config_filename) as stream:
            config = yaml.load(stream)
        if config is None:
            config = {}
    except IOError:
        config = {}

    # Warnings that should be seen only once
    config['_once_warnings'] = []

    # Process config
    if 'io' in config:
        if 'count_tables' in config['io']:
            for tablename, sheet in config['io']['count_tables'].items():
                config['io']['count_tables'][tablename] = _normalize_count_table(sheet)

        if 'samplesheets' in config['io']:
            for sheetname, sheet in config['io']['samplesheets'].items():
                config['io']['samplesheets'][sheetname] = _normalize_samplesheet(sheet)

        if 'featuresheets' in config['io']:
            for sheetname, sheet in config['io']['featuresheets'].items():
                config['io']['featuresheets'][sheetname] = _normalize_featuresheet(sheet)

        if 'datasets' in config['io']:
            for datasetname, dataset in config['io']['datasets'].items():
                config['io']['datasets'][datasetname] = _normalize_dataset(dataset)

    return config


config = reload_config()
