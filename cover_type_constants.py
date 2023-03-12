
# No se tienen caracterisiticas categoricas debido al subconjunto de puntos anteriores
CATEGORICAL_FEATURE_KEYS = ['Cover_Type']

# Numerical features that are marked as continuous
NUMERIC_FEATURE_KEYS = [
    'Elevation', 'Hillshade_9am', 'Hillshade_Noon', 'Horizontal_Distance_To_Fire_Points',
    'Horizontal_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Slope',
    'Vertical_Distance_To_Hydrology'
]

# Feature that can be grouped into buckets
BUCKET_FEATURE_KEYS = ['Slope']

# Number of buckets used by tf.transform for encoding each bucket feature.
FEATURE_BUCKET_COUNT = {'Slope': 4}

# Feature that the model will predict
LABEL_KEY = 'Cover_Type'

# Utility function for renaming the feature
def transformed_name(key):
    return key + '_xf'
