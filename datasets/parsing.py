from .main import ConversationDataset

from utils import is_vk_object, load_all_dialog
from methods.messages import get_history
from config import API_VERSION


def create_conv_dataset(access_token, peer, v=API_VERSION, **parameters):
    """
    This function is used to create conversation dataset from zero, using only token and peer
    """
    if is_vk_object(peer):
        peer = peer['id']
    params = {
        'v': v,
        'access_token': access_token,
        'peer_id': peer
    }
    params.update(parameters)

    data = load_all_dialog(params)

    return ConversationDataset(data['items'])

