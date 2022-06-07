from os import path
import pandas as pd


class DataLoader:
    def __init__(self, data_path):
        self._badges_df = pd.read_xml(path.join(data_path, 'Badges.xml'))
        self._comments_df = pd.read_xml(path.join(data_path, 'Comments.xml'))
        self._postHistory_df = pd.read_xml(path.join(data_path, 'PostHistory.xml'))
        self._postLinks_df = pd.read_xml(path.join(data_path, 'PostLinks.xml'))
        self._posts_df = pd.read_xml(path.join(data_path, 'Posts.xml'))
        self._tags_df = pd.read_xml(path.join(data_path, 'Tags.xml'))
        self._users_df = pd.read_xml(path.join(data_path, 'Users.xml'))
        self._votes_df = pd.read_xml(path.join(data_path, 'Votes.xml'))