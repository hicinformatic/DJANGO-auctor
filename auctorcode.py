import re

class AuctorTag(object):
    pattern_open = re.compile(r"\[\{ac-?(\w+):?\(?([a-zA-Z0-9=\-\"# :;\.\/&]+)?\)?\}\]", re.MULTILINE)
    pattern_close = re.compile(r"\[\{ac(\/?\w+)\}\]", re.MULTILINE)

class AuctorAttribute(object):
    test_case ="""
    class="linux" style="color: #888; padding: 5px; font-weight: bold;" height="400"
    class="linux" style="color: #888; padding: 5px; font-weight: bold;"
    style="color: #888; padding: 5px; font-weight: bold;"
    """
    pattern = re.compile(r"[ |\(]([a-zA-Z0-9&]+)=\"([a-zA-Z0-9:\ #;\-]+)\"", re.MULTILINE)

class AuctorCode(object):
    conf_tag = AuctorTag()
    conf_attr = AuctorAttribute()
    tags = {
        'anchor':   { 'tag': 'a', },
        'link':     { 'tag': 'a', },
        'section':  { 'tag': 'section', 'attributes': ['style', 'height', 'width'], },
        'article':  { 'tag': 'article', 'attributes': ['style', 'height', 'width'], },
        'title1':   { 'tag': 'h1',      'attributes': ['style', 'height', 'width'], },
        'title2':   { 'tag': 'h2',      'attributes': ['style', 'height', 'width'], },
        'title3':   { 'tag': 'h3',      'attributes': ['style', 'height', 'width'], },
        'title4':   { 'tag': 'h4',      'attributes': ['style', 'height', 'width'], },
        'title5':   { 'tag': 'h5',      'attributes': ['style', 'height', 'width'], },
        'title6':   { 'tag': 'h6',      'attributes': ['style', 'height', 'width'], },
        'para':     { 'tag': 'p' ,      'attributes': ['style', 'height', 'width'],},
        'list':     { 'tag': 'ul',      'attributes': ['style', 'height', 'width'], },
        'listord':  { 'tag': 'ol',      'attributes': ['style', 'height', 'width'], },
        'puce':     { 'tag': 'li',      'attributes': ['style', 'height', 'width'], },
        'img':      { 'tag': 'img',     'attributes': ['style', 'height', 'width', 'src'], },
        'code':     { 'tag': 'pre',     'attributes': ['style', 'height', 'width'], },
        'terminal': { 'tag': 'pre',     'attributes': ['style', 'height', 'width'], },
        'termcmd':  { 'tag': 'pre',     'attributes': ['style', 'height', 'width'], },
        'termout':  { 'tag': 'pre',     'attributes': ['style', 'height', 'width'], },
    }
    attributes = {
        'style': { 'attribute': 'style', 'pattern': re.compile(r"([a-zA-Z0-9:\ #;\-]+)") },
        'link':  { 'attribute': 'src',   'pattern': re.compile(r"'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+") },
    }

    pattern_open = r"\[\{ac-(%s)(:\()?(%s[\w\d\s[:punct:]]+)?\)?\}\]"
    pattern_close = r"\[\{ac-(%s)\}\]"
    tag_pattern_match = None
    tag_pattern_replace = None
    attribute_pattern_match = None
    attribute_pattern_replace = None
    content_input = None
    content_output = None

    def prepare(self):
        self.tag_pattern_match = '|'.join(self.tags.keys())
        self.tag_pattern_replace = '|'.join([tag['tag'] for key,tag in self.tags.items()])
        self.attribute_pattern_match = '|'.join(self.attributes.keys())
        self.attribute_pattern_replace = '|'.join([attribute['attribute'] for key,attribute in self.attributes.items()])

    def to_html(self, text):
            matches = self.conf_tag.pattern_open.findall(text)
            #for match in matches:
               # if match[0] not in self.tags:
               #     print('no')
            text = self.conf_tag.pattern_open.sub(r'<\1 \2>', text)
            text = self.conf_tag.pattern_close.sub(r'<\1>', text)
            #self.content = self.conf_tag.pattern_close.sub(r'<\1>', self.content)
            return text
        #return 'ko'


        