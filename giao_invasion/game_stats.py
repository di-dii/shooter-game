import json

class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self,ai_settings):
        '''初始化统计信息'''
        self.ai_settings=ai_settings
        self.reset_stats()

        #让游戏一开始处于非活动状态
        self.game_active=False

        #任何情况下都不应重置最高分
        self.high_score=self.read_high_score()

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1

    def read_high_score(self):
        self.high_score_doc_path='high score record.json'
        try:
            with open(self.high_score_doc_path,'r') as file_obj:
                record_score=json.load(file_obj)
        except FileNotFoundError:
            return 0
        else:
            return record_score

    def store_high_score(self):
        with open(self.high_score_doc_path,'w') as file_obj:
            json.dump(self.high_score,file_obj)


