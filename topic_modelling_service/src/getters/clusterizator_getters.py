from models.topic_moddeling_body_models import TopicModellingBody
from sklearn.cluster import KMeans


def clusterizator_getter(data: TopicModellingBody):
    if data.max_num_of_topics == None:
        return None
    return KMeans(
        n_clusters=data.max_num_of_topics
    )
