import grasshook.collector
import grasshook.collectors
import os
import tables
import yaml
import grasshook.data

def parse_config(config_file):
    with open(config_file, 'rb') as f:
        return yaml.safe_load(f.read())

def open_h5(data_file):
    if os.path.exists(data_file):
        # return pointer to existing database
        return tables.open_file(data_file, mode="a")
    else:
        # create and setup new database
        h5file = tables.open_file(data_file, mode='w')
        group = h5file.create_group("/", "gh")
        table = h5file.create_table(group, "ghdata", grasshook.data.Data, "Colleted data.")
        return h5file

def run():
    config_file = "config.yaml"
    data_filename = "data.h5"

    data = parse_config(config_file)
    data_file = open_h5(data_filename)
    table = data_file.root.gh.ghdata

    for alias, info in data.iteritems():
        collector = grasshook.collector.Collector.create_instance(alias, info)
        collector.collect(table.row)

    table.flush()
    data_file.close()
