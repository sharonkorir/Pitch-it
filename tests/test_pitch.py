from app.models import Comment,User, Pitch
from app import db

#comments
def setUp(self):
        self.user_Sharon = User(username = 'Sharon',password = 'foobar', email = 'sharon@email.com')
        self.new_comment = Comment(pitch_id=12,user_id=1, comment='lol')

def tearDown(self):
        Comment.query.delete()
        User.query.delete()

def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

'''
#pitches
def setUp(self):
        self.user_Sharon = User(username = 'Sharon',password = 'foobar', email = 'sharon@email.com')
        self.new_pitch = Pitch(id=12,  comment_)

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)
'''