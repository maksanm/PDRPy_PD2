from os import path
import pandas as pd


class DataLoader:
    def __init__(self, data_path):
        self.badges_df = pd.read_xml(path.join(data_path, 'Badges.xml'))
        self.comments_df = pd.read_xml(path.join(data_path, 'Comments.xml'))
        self.postHistory_df = pd.read_xml(path.join(data_path, 'PostHistory.xml'))
        self.postLinks_df = pd.read_xml(path.join(data_path, 'PostLinks.xml'))
        self.posts_df = pd.read_xml(path.join(data_path, 'Posts.xml'))
        self.tags_df = pd.read_xml(path.join(data_path, 'Tags.xml'))
        self.users_df = pd.read_xml(path.join(data_path, 'Users.xml'))
        self.votes_df = pd.read_xml(path.join(data_path, 'Votes.xml'))
