from django.test import TestCase
from .models import Image,Profile

# Create your tests here.
class ImageTestClass(TestCase):
    """
    Test for testing the image class
    """
    def setUp(self):
        self.new_image=Image(image_name="food",image_caption="Where the sun never sets",likes="12",comments="Eeeey")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def tearDown(self):
        Image.objects.all().delete()

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertEqual(len(images),1)

    def test_delete_method(self):
        self.Image.delete_image()
        images=Image.objects.all()
        self.assertEqual(len(Image),1)

    def test_updatecaption_method(self):
        self.Image.update_caption()
        images=Image.objects.all()
        self.assertEqual(len(images),1)

class ProfileTestClass(TestCase):
    '''
    Test for testing the profile class
    '''

    def setUp(self):
        self.new_profile=Profile()
