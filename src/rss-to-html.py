#
# RSS-to-HTML
# Copyright (C) 2024
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from jinja2 import Environment, FileSystemLoader
import feedparser
import time
import requests
import configparser
import re


# <editor-fold desc="Utils">


def has_attribute(obj, attr: str) -> bool:
    if obj is None:
        return False
    if not hasattr(obj, attr):
        return False
    if getattr(obj, attr) is None or getattr(obj, attr) == '':
        return False
    return True


def sanitize_content(possible_html_content: str) -> str:
    possible_html_content = possible_html_content.strip()
    result = re.search(r"</?\s*[a-z-][^>]*\s*>|(&(?:[\w\d]+|#\d+|#x[a-f\d]+);)", possible_html_content)
    if result is not None:
        if possible_html_content.startswith("<p>") and possible_html_content.endswith("</p>"):
            possible_html_content = possible_html_content[3:-4]
        return possible_html_content.strip()
    return possible_html_content.replace("\n", "<br>")


# </editor-fold desc="Utils">


# Parse the main config values
config = configparser.ConfigParser()
config.read('application.cfg')
rss_feed_url = config['DEFAULT']['RssFeedUrl']
template_name = config['DEFAULT']['TemplateName']
output_file = config['DEFAULT']['HtmlFileOutput']

# Fetch the RSS content
site_request = requests.get(rss_feed_url, verify=False)
site_response = site_request.content
rss = feedparser.parse(site_response)

# Deploy the template
environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template("templates/" + template_name)
content = template.render(
    rss=rss,
    config=config,
    rss_feed_url=rss_feed_url,
    has_attribute=has_attribute,
    sanitize_content=sanitize_content,
    strftime=time.strftime,
)

# Write down the result
with open(output_file, mode="w", encoding="utf-8") as output:
    output.write(content)
    print(f"... wrote {output_file}")
