from __future__ import division
import numpy as np
# import cv2
import time, io
# from matplotlib import pyplot as plt
from google.cloud import vision
from google.cloud.vision.feature import Feature,FeatureTypes

MIN_MATCH_COUNT = 200
# only using match count right now
MIN_MATCH_RATIO = .2

NUM_LABELS = 20
NUM_LANDMARKS = 3
NUM_LOGOS = 3

MIN_SCORE = 0

def compare(img1_name, img2_name):
    """
    Return whether img1 and img2 differ signficiantly

    Determined through feature matching and comparison
    (the number of good matches must be greater than MIN_MATCH_COUNT)
    """
    img1 = cv2.imread(img1_name)
    img2 = cv2.imread(img2_name)
    #  Initiate SIFT detector
    sift = cv2.xfeatures2d.SURF_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # count the number of good matches
    num_good_matches = 0
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            num_good_matches += 1
    print('Number of good features matched: ' + str(num_good_matches))
    return num_good_matches>MIN_MATCH_COUNT

def get_features(img_path):
    """
    Returns a list of features from an image

    Optionally pass a certainty_threshold value to give a threshold in [0,1] on how certain
    Google's identification is.
    """
    v_c = vision.Client()
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    img = v_c.image(content=content)
    output = []
    features = [Feature(FeatureTypes.LABEL_DETECTION, NUM_LABELS),
                Feature(FeatureTypes.LANDMARK_DETECTION, NUM_LANDMARKS),
                Feature(FeatureTypes.LOGO_DETECTION, NUM_LOGOS)]
    annotations = img.detect(features)
    for label in annotations[0].labels:
        if label.score >= MIN_SCORE:
            output.append(label.description.encode('utf-8'))
    for landmark in annotations[0].landmarks:
        if landmark.score >= MIN_SCORE:
            output.append(landmark.description.encode('utf-8'))
    for logo in annotations[0].logos:
        if logo.score >= MIN_SCORE:
            output.append(logo.description.encode('utf-8'))
    return output

def has_features(img_path, features):
    """
    Returns whether or not features are in the image provided.
    """
    f = get_features(img_path)
    for feature in features:
        if feature in f:
            return True
    return False

