import json
import matplotlib.pyplot as plt
import pickle
import random as rnd

def image_filter(lower_included, higher_included):

    with open("cityscapes_train.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    images = jsonObject['images']
    annotations = jsonObject['annotations']

    image_ids = []
    instances = []
    instance_count = []

    # get image ids from json, here [1, 2,..., 2974]
    for image in images:
        image_ids.append(image['id'])

    # count number of instances per image
    for instance in annotations:
        instances.append(instance['image_id'])
    for i in image_ids:
        instance_count.append(instances.count(i))

    # filter image ids to a list with images with 'instance_threshold' or more persons in it
    filtered_image_ids = []
    for i, num in enumerate(instance_count):
        if higher_included >= num and num >= lower_included:
            filtered_image_ids.append(i)

    print('Images with following ID:')
    print(image_ids)
    print('contain following amount of instances correspondingly:')
    print(instance_count)
    print('And '+str(len(filtered_image_ids))+' images with follwoing IDs contains between '+str(lower_included)+' and '+str(higher_included)+' instances:')
    print(filtered_image_ids)

    # create optional a histogram of the distributon of images and the amount of image instances
    plt.ylabel('number of images')
    plt.xlabel('number of person')
    plt.title('Instance Distribution')
    plt.hist(instance_count, bins=range(0, 41))
    plt.savefig('instance_num_hist6.png')


    return filtered_image_ids


# create a random list
if __name__ == '__main__':
    # create a list of image ids filtered after above conditions
    filtered_list = image_filter(21, 29)

    # create a random list of these filtered images
    # comment out after generation to not accidentally change the new random list pickle
    random_list = []
    '''
    while(len(random_list)<=100-1):
        random_element = rnd.choice(filtered_list)
        if not random_list.__contains__(random_element):
            random_list.append(random_element)

    print(len(random_list))
    print(random_list)

    with open("random_list_21-29.txt", "wb") as fp:
        pickle.dump(random_list, fp)
    '''
