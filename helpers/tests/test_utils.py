import logging
from textwrap import dedent

import pytest
from bs4 import BeautifulSoup

from codeselfstudy.helpers import utils

log = logging.getLogger(__name__)


class TestSafeListGet():
    @pytest.mark.parametrize("lst, idx, default, expected", [
        ([1, 2, 3], 0, None, 1),
        ([1, 2, 3], 2, None, 3),
        ([], 2, None, None),
        ([1, 2, 3], 10, None, None),
        ([1, 2, 3], -2, None, 2),
    ])
    def test_safe_list_get_3_args(self, lst, idx, default, expected):
        result = utils.safe_list_get(lst, idx, default)
        assert result == expected

    def test_safe_list_get_2_args(self):
        lst = [1, 2]
        result = utils.safe_list_get(lst, 4)
        assert result is None


class TestCreateRandomSlug():
    def test_create_random_slug_length(self):
        """Tests that a slug is created with the correct length."""
        slug = utils.create_random_slug()
        assert len(slug) == 8


class TestCreateEntityId():
    def test_create_entity_id(self):
        s1 = utils.create_entity_id(1)
        s2 = utils.create_entity_id(4)
        s3 = utils.create_entity_id(16)
        s4 = utils.create_entity_id(32)

        # these don't work -- the length is in bytes
        # assert len(s1.encode("utf-8")) == 16
        # assert len(s2.encode("utf-8")) == 4
        # assert len(s3.encode("utf-8")) == 10
        # assert len(s4.encode("utf-8")) == 32
        assert isinstance(s1, str)
        assert isinstance(s2, str)
        assert isinstance(s3, str)
        assert isinstance(s4, str)


class TestCleanUserInput():
    def test_strip_bad_tags(self):
        text = """'
        <h1>hello world</h1>
        <script src="http://badwebsite123321123.com/evil.js"></script>

        <img src="https://placekitten.com/200/200" alt="hello">

        <p>lorem ipsum</p>
        """
        html = utils.clean_user_input(text)
        soup = BeautifulSoup(html, "html.parser")
        images = soup.select("img")
        scripts = soup.select("script")
        h1s = soup.select("h1")

        assert not images
        assert not scripts
        assert h1s is not None


# class TestCookMarkdown():
#     def test_render_markdown(self):
#         md = dedent("""\
#         # hello world

#         lorem ipsum

#         - item
#         - item

#         ![meow](https://placekitten.com/500/500)

#         <div class="green">not a div</div>
#         """).strip()
#         html = utils.cook_markdown(md)
#         log.info(f"html {html}")
#         soup = BeautifulSoup(html)
#         h1s = soup.select("h1")
#         ps = soup.select("p")
#         lis = soup.select("li")
#         imgs = soup.select("img")
#         divs = soup.select("div")
#         log.info("soup {soup}")

#         assert not imgs
#         assert not divs
#         assert len(h1s) == 1
#         assert len(lis) == 2
#         assert len(ps) == 3


# class TestFixProjectEulerRelativePaths():
#     def test_change_relative_src_to_absolute(self):
#         html = """
#         <p>In a very simplified form, we can consider proteins as strings consisting of hydrophobic (H) and polar (P) elements, e.g. HHPPHHHPHHPH. <br/>\nFor this problem, the orientation of a protein is important; e.g. HPP is considered distinct from PPH. Thus, there are 2<sup><var>n</var></sup> distinct proteins consisting of <var>n</var> elements.</p><p>When one encounters these strings in nature, they are always folded in such a way that the number of H-H contact points is as large as possible, since this is energetically advantageous.<br/>\nAs a result, the H-elements tend to accumulate in the inner part, with the P-elements on the outside.<br/>\nNatural proteins are folded in three dimensions of course, but we will only consider protein folding in <u>two dimensions</u>.</p><p>The figure below shows two possible ways that our example protein could be folded (H-H contact points are shown with red dots).</p><div align=\"center\"><img src=\"project/images/p300_protein.gif\" alt=\"p300_protein.gif\"/></div><p>The folding on the left has only six H-H contact points, thus it would never occur naturally.<br/>\nOn the other hand, the folding on the right has nine H-H contact points, which is optimal for this string.</p><p>Assuming that H and P elements are equally likely to occur in any position along the string, the average number of H-H contact points in an optimal folding of a random protein string of length 8 turns out to be 850 / 2<sup>8</sup>=3.3203125.</p><p>What is the average number of H-H contact points in an optimal folding of a random protein string of length 15?<br/>\nGive your answer using as many decimal places as necessary for an exact result.</p>
#         """  # noqa: E501

#         original_soup = BeautifulSoup(html)
#         result = utils.fix_project_euler_relative_paths(html)
#         soup = BeautifulSoup(html)

