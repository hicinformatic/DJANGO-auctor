from django.test import TestCase

# Create your tests here.
class AuctorCodeTestCase(TestCase):
    text_testcase = """
    [{ac-section}]
        [{ac-title:(style="color: #888;")}]Section title[{ac/title}]
        [{ac-article}]
            [{ac-title}]Article title[{ac/title}]
            [{ac-para}]Lorem ipsum dolor sit amet, consectetur adipiscing elit.[{ac-smiley-laugh)}][{ac/para}]
        [{ac/article}]

        [{ac-article}]
            [{ac-title}]Article title[{ac/title}]
            [{ac-para:(style="color: #888" height="400")}]
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                [{ac-img:(src="https://url/img.jpg")}]
                [{ac-list}]
                    [{ac-puce}]puce 1[{ac/puce}]
                    [{ac-puce}]puce 2[{ac/puce}]
                [{ac/list}]
            [{ac/para}]
        [{ac/article}]

        [{ac-code:(class="ac-php")}]
            if ($test) {
                echo "test";
            }
        [{ac/code}]

        [{ac-terminal:(class="linux")}]
            [{ac-termcmd:(class="linux")}]ps -ef[{ac/termcmd}]
            [{ac-termout:(class="linux")}]root       2157      2  0 09:56 ?        00:00:26 [kworker/0:2][{ac/termout}]
            [{ac-termout:(class="linux")}]root       3277      2  0 14:08 ?        00:00:00 [kworker/0:1][{ac/termout}]
        [{ac/terminal}]
    [{ac/section}]
    """

    def test_auctor_regex(self):
        from pprint import pprint
        from auctor.auctorcode import AuctorCode
        ac = AuctorCode()
        ac.prepare()
        print('tags match: \n%s\n' % ac.tag_pattern_match)
        print('tags replace: \n%s\n' % ac.tag_pattern_replace)
        print('attributes match: \n%s\n' % ac.attribute_pattern_match)
        print('attributes replace: \n%s\n' % ac.attribute_pattern_replace)

    def test_auctor_tohtml(self):
        from pprint import pprint
        from auctor.auctorcode import AuctorCode
        ac = AuctorCode()
        ac.prepare()
        #print(ac.to_html(self.text_testcase))

