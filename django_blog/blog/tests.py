from django.urls import reverse, resolve

def test_urls():
    assert reverse('blog:comment-create', kwargs={'post_id': 1}) == '/posts/1/comments/new/'
    assert reverse('blog:comment-update', kwargs={'pk': 1}) == '/comment/1/update/'
    assert reverse('blog:comment-delete', kwargs={'pk': 1}) == '/comment/1/delete/'
