from objects.main import *

OBJECT_NAMES = {
    'user': User,
    'wall': Post,
    'post': Post,
    'message': Message
}

__all__ = [
    'VKObject',
    'User',
    'Post',
    'Message'
]
