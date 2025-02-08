import os
# from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader,  TextLoader
import json



def get_document_text(json_file_path, dict_file_path):
    with open(json_file_path, 'r') as file:
        data_str = file.read()
    data = json.loads(data_str)

    res_dict = dict()
    for item in data:
        if item['id'] not in res_dict:
            res_dict[item['id']] = item
        else:
            print (item['id'])

    loader = DirectoryLoader(dict_file_path, glob="**/*.txt", loader_cls=TextLoader)
    data = loader.load()
    # print(data)

    # Split the text into Chunks
    for item in data:
        item.metadata['date'] = res_dict[item.metadata['source'][11:-4]]['date'][:10]

    return data
