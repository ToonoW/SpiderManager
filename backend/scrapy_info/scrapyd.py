from backend.models import Scrapyd


def add_node(node):
    """
    增加scrapyd节点

    在这里需要每个字段都设置，否则不为空字段不设置值内容会被默认填充''
    :param node: 节点的字典信息
    :return:
    """
    scrapyd = Scrapyd()
    fields = Scrapyd._meta.get_fields()[1:]     # 跳过第一个field 'ID'
    for field in fields:
        value = node.get(field.name)
        setattr(scrapyd, field.name, value)
    scrapyd.save()