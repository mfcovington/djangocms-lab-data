import collections
import operator

def get_data_list_tags(data_list):
    data_list_tags = {}

    for data_item in data_list:
        for tag in data_item.tags.all():
            data_list_tags[tag.id] = tag.name

    data_list_tags = collections.OrderedDict(
        sorted(data_list_tags.items(), key=operator.itemgetter(1)))

    return data_list_tags
