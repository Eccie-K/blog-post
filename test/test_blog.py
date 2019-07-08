import unittest
from app.models import Blog, User
from app import db

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User(username = 'Esther',password = 'liver', email = 'esther@gmail.com')
        self.new_post = Post(id=12,title='Just Live',post_content='Hard work pays off',blog_category="blog blog",user = self.user_Eccie)
    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,12)
        self.assertEquals(self.new_post.title,'Go Home')
        self.assertEquals(self.new_post.post_content,'Do or die')
        self.assertEquals(self.new_post.post_category,"Blog blog")
        self.assertEquals(self.new_post.user,self.user_James)
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_post = Post.get_post(12)
        self.assertTrue(got_post is not None)

if __name__ == '__main__':
  unittest.main()
