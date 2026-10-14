"""Check that each localized landing page exposes a usable raster link preview."""

import struct
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE_URL = "https://radimoo.com/assets/social-preview.png"


class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            self.tags[attrs.get("property", attrs.get("name"))] = attrs.get("content")


class SocialPreviewTests(unittest.TestCase):
    def test_preview_is_a_publishable_png(self):
        image = (ROOT / "assets/social-preview.png").read_bytes()
        self.assertEqual(image[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", image[16:24]), (1024, 500))
        self.assertLess(len(image), 2_000_000)

    def test_localized_landing_pages_share_raster_metadata(self):
        for locale in ("", "ko", "ja", "zh-cn", "zh-tw"):
            with self.subTest(locale=locale):
                tags = Metadata((ROOT / locale / "index.html").read_text()).tags
                self.assertEqual(tags["og:image"], IMAGE_URL)
                self.assertEqual(tags["twitter:image"], IMAGE_URL)
                self.assertEqual(tags["og:image:type"], "image/png")
                self.assertEqual(tags["og:image:width"], "1024")
                self.assertEqual(tags["og:image:height"], "500")
                self.assertTrue(tags["og:image:alt"])
                self.assertEqual(tags["twitter:image:alt"], tags["og:image:alt"])
                self.assertEqual(tags["twitter:card"], "summary_large_image")


if __name__ == "__main__":
    unittest.main()
