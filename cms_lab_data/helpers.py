import collections
import operator

def get_data_file_list_tags(data_file_list):
    data_file_list_tags = {}

    for data_file in data_file_list:
        for tag in data_file.tags.all():
            data_file_list_tags[tag.id] = tag.name

    data_file_list_tags = collections.OrderedDict(
        sorted(data_file_list_tags.items(), key=operator.itemgetter(1)))

    return data_file_list_tags
