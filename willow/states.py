class ImageState(object):
    @classmethod
    def check(cls):
        pass

    @staticmethod
    def operation(func):
        func._willow_operation = True
        return func

    @staticmethod
    def converter_to(state_class):
        def wrapper(func):
            func._willow_converter_to = state_class
            return func

        return wrapper

    @staticmethod
    def converter_from(state_class):
        def wrapper(func):
            if not hasattr(func, '_willow_converter_from'):
                func._willow_converter_from = []
            func._willow_converter_from.append(state_class)
            return func

        return wrapper


# Buffer states

class ImageBufferState(ImageState):
    def __init__(self, size, data):
        self.size = size
        self.data = data

    @ImageState.operation
    def get_size(self):
        return self.size


class RGBImageBufferState(ImageBufferState):
    mode = 'RGB'

    @ImageState.operation
    def has_alpha(self):
        return False

    @ImageState.operation
    def has_animation(self):
        return False


class RGBAImageBufferState(ImageBufferState):
    mode = 'RGBA'

    @ImageState.operation
    def has_alpha(self):
        return True

    @ImageState.operation
    def has_animation(self):
        return False


# File States

class ImageFileState(ImageState):
    def __init__(self, f):
        self.f = f


class JPEGImageFileState(ImageFileState):
    pass


class PNGImageFileState(ImageFileState):
    pass


class GIFImageFileState(ImageFileState):
    pass
