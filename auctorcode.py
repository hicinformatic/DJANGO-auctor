import re

class AuctorCode(object):
    content_ac = None
    class tag(object):
        name = None
        tag = None
        pattern = '\[([[:alpha:]]+)\](.*)\[/([[:alpha:]]+)]'

    class attribute(object):
        name = None
        attribute = None
        pattern = '\|%s(\(.+\))'
        replace = ' %s="%s"'

    class href(attribute):
        name = 'href'
        attribute = 'href'

    class link(tag):
        name = 'link'
        tag = 'a'

    def __init__(self, content_ac):
        self.content_ac = content_ac
    
    def Encoding(self):
        return re.sub(self.tag.pattern, self.Replacing, self.content_ac)

    def Replacing(self, matchobj):
        from pprint import pprint
        pprint(matchobj)
        return 'test'
        #return "<%s>" % getattr(getattr(self, matchobj.group(2)), tag)
        