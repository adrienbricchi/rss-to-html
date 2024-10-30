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

max_score = 100
test_name = "Python Challenge"
episodes = [
    {"guid": "3010801bde7649ea9777ea84fcb6e343", "title": "Fesse-hugger (Alien Romulus)"},
    {"guid": "f1ff11110aed4c5580e2ecc697e52fdc", "title": "Vomir c'est repartir (Qui a peur de Virginia Woolf ?)"},
]

environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template("card_template.j2")

content = template.render(
    episodes= episodes,
    title='Le Podcast sans visage',
    main_image='https://lepodcastsansvisage.fr/media/fanart.jpg',
)

filename = f"index.html"
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote {filename}")
