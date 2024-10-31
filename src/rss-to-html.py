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

# Parse the main config values
config = configparser.ConfigParser()
config.read('application.cfg')
url = config['DEFAULT']['RssFeedUrl']
template_name = config['DEFAULT']['TemplateName']
output_file = config['DEFAULT']['HtmlFileOutput']

# Fetch the RSS content
site_request = requests.get(url, verify=False)
site_response = site_request.content
rss = feedparser.parse(site_response)

# Deploy the template
environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template("templates/" + template_name)
content = template.render(
    rss=rss,
    config=config,
    strftime=time.strftime,
)

# Write down the result
with open(output_file, mode="w", encoding="utf-8") as output:
    output.write(content)
    print(f"... wrote {output_file}")
