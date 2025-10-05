# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')
        self.post = Post.objects.create(title='Test', content='Test content', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('blog:post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test')

    def test_detail_view(self):
        resp = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post_create'))
        self.assertNotEqual(resp.status_code, 200)  # redirect to login
        self.client.login(username='author', password='pass12345')
        resp = self.client.get(reverse('blog:post_create'))
        self.assertEqual(resp.status_code, 200)

    def test_update_by_author(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post_edit', kwargs={'pk': self.post.pk}),
                                {'title': 'Updated', 'content': 'Updated content'})
        self.assertEqual(resp.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')

    def test_update_not_by_author_forbidden(self):
        self.client.login(username='other', password='pass12345')
        resp = self.client.get(reverse('blog:post_edit', kwargs={'pk': self.post.pk}))
        # Should be forbidden or redirect (UserPassesTestMixin returns 403 by default)
        self.assertIn(resp.status_code, (302, 403))

    def test_delete_by_author(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')
        self.post = Post.objects.create(title='Test', content='Test content', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('blog:post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test')

    def test_detail_view(self):
        resp = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post_create'))
        self.assertNotEqual(resp.status_code, 200)  # redirect to login
        self.client.login(username='author', password='pass12345')
        resp = self.client.get(reverse('blog:post_create'))
        self.assertEqual(resp.status_code, 200)

    def test_update_by_author(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post_edit', kwargs={'pk': self.post.pk}),
                                {'title': 'Updated', 'content': 'Updated content'})
        self.assertEqual(resp.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')

    def test_update_not_by_author_forbidden(self):
        self.client.login(username='other', password='pass12345')
        resp = self.client.get(reverse('blog:post_edit', kwargs={'pk': self.post.pk}))
        # Should be forbidden or redirect (UserPassesTestMixin returns 403 by default)
        self.assertIn(resp.status_code, (302, 403))

    def test_delete_by_author(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
