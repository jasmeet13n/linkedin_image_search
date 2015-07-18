import os
import urllib

if __name__ == "__main__":
    f = open("linkedin_profiles.csv", 'rb')
    for line in f.readlines():
        line = line.split(',')
        image_url = line[1].replace("\n", "")
        url = line[0].replace("https://", "").replace("/", " ")
        print url
        print image_url.replace("/", " ")

        dir_path = "linkedInHackData/" + url
        if not os.path.exists(dir_path):
                os.makedirs(dir_path)

        urllib.urlretrieve(image_url, dir_path + "/" + "1.jpg")
        urllib.urlretrieve(image_url, dir_path + "/" + "2.jpg")
        urllib.urlretrieve(image_url, dir_path + "/" + "3.jpg")
