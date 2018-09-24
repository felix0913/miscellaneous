from conf import settings

def pack():
    response = {}
    for k,v in settings.PLUGINS:
        import importlib
        m_path, class_name = v.rsplit('.', maxsplit=1)
        m = importlib.import_module(m_path)
        cls = getattr(m, class_name)
        response[k] = cls().execute()

    return response