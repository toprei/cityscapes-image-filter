import json
import pickle

if __name__ == '__main__':

    images_list = []
    annotations_list = []

    # load created filtered random image list and cityscapes annotation file
    with open("random_list_21-29.txt", "rb") as fp:
        filtered_list_random = pickle.load(fp)
    with open("cityscapes_train.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    images = jsonObject['images']
    annotations = jsonObject['annotations']

    # set wished length of dataset
    #dataset_size = 100

    # truncate filtered random list to 'dataset_size' first images
    #del filtered_list_random[dataset_size:]

    # create coco annotation json file for these images
    for id, image_obj in enumerate(images):
        if filtered_list_random.__contains__(image_obj['id']):
            images_list.append(image_obj)
    for id, annotation_obj in enumerate(annotations):
        if filtered_list_random.__contains__(annotation_obj['image_id']):
            annotations_list.append(annotation_obj)

    print("start creating json")
    json_data = {
        "images": images_list,
        "categories": [{"id": 1, "name": "person"}],
        "annotations": annotations_list
    }
    print("start dumping json")
    with open('cityscapes_train_21-29.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close()

    print("done!")
