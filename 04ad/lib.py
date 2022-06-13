import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

import joblib
import os

import lightgbm as lgb

from sklearn import preprocessing
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')


categorical = [
    'c_user_gender', 
    'c_user_age', 
    'c_content_flag_used', 
    'c_content_category_id_1', 
    'c_content_category_id_2', 
    'c_content_category_id_3']

continuous = [
    'user_following_count', 
    'user_pay_count', 
    'advertiser_grade', 
    'advertiser_item_count',
    'advertiser_interest_count', 
    'advertiser_follower_count', 
    'advertiser_pay_count', 
    'advertiser_review_count',
    'advertiser_parcel_post_count', 
    'advertiser_transfer_count', 
    'advertiser_chat_count', 
    'advertiser_favorite_count',
    'advertiser_comment_count', 
    'content_bid_price', 
    'content_price', 
    'content_emergency_count', 
    'content_comment_count', 
    'content_interest_count', 
    'content_favorite_count']

features = categorical + continuous

candidate_features = [
    'advertiser_grade',
    'advertiser_item_count', 
    'advertiser_interest_count',
    'advertiser_follower_count', 
    'advertiser_pay_count',
    'advertiser_review_count', 
    'advertiser_parcel_post_count',
    'advertiser_transfer_count', 
    'advertiser_chat_count',
    'advertiser_favorite_count', 
    'advertiser_comment_count',
    'content_bid_price', 
    'content_price', 
    'c_content_flag_used',
    'c_content_category_id_1', 
    'c_content_category_id_2',
    'c_content_category_id_3', 
    'content_emergency_count',
    'content_comment_count', 
    'content_interest_count',
    'content_favorite_count', 
    'content_id', 
    'content_img_url']


def process_missing_values(df):
    for categorical_col in categorical:
        df[categorical_col] = df[categorical_col].astype(str)
        df[categorical_col] = df[categorical_col].fillna('0')
        df[categorical_col] = preprocessing.LabelEncoder().fit_transform(df[categorical_col])

    for continuous_col in continuous:
        df[continuous_col] = df[continuous_col].fillna(0)

    return df
