from beets.plugins import BeetsPlugin
from beets.ui.commands import PromptChoice
from beets import importer
import shutil
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class DropPlugin(BeetsPlugin):
    def __init__(self):
        super(DropPlugin, self).__init__()
        self.register_listener('before_choose_candidate',
                               self.before_choose_candidate_event)

    def before_choose_candidate_event(self, session, task):
        return [PromptChoice('n', 'iNcomplete', self.incomplete),
            PromptChoice('c', 'unClassified', self.unclassified)]

    def incomplete(self, session, task):
        #self.import_stages = [self.move_folder_to_incomplete]
        self.move_folder_to_incomplete(session, task)
        return importer.action.SKIP

    def unclassified(self, session, task):
        #self.import_stages = [self.move_folder_to_unclassified]
        self.move_folder_to_unclassified(session, task)
        return importer.action.SKIP

    def move_folder_to_incomplete(self, session, task):
        for p in task.paths:
            shutil.move(p,
                self.config['incomplete'].get() + p[len(task.toppath):len(p)])

    def move_folder_to_unclassified(self, session, task):
        for p in task.paths:
            shutil.move(p.encode('utf8'),
                self.config['unclassified'].get() + p[len(task.toppath):len(p)])
