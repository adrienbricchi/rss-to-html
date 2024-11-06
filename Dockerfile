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

FROM python:3.9.20-bookworm@sha256:ed8b9dd4e9f89c111f4bdb85a55f8c9f0e22796a298449380b15f627d9914095

# Open Containers Initiative parameters
ARG CI_COMMIT_REF_NAME=""
ARG CI_COMMIT_SHA=""
ARG CI_PIPELINE_CREATED_AT=""
# Non-standard and/or deprecated variables, that are still widely used.
# If it is already set in the FROM image, it has to be overridden.
MAINTAINER Adrien BRICCHI
LABEL maintainer="Adrien BRICCHI"
LABEL org.label-schema.build-date="$CI_PIPELINE_CREATED_AT"
LABEL org.label-schema.name="rss-to-html"
LABEL org.label-schema.schema-version="1.0"
# Open Containers Initiative's image specifications
LABEL org.opencontainers.image.authors="Adrien BRICCHI"
LABEL org.opencontainers.image.created="$CI_PIPELINE_CREATED_AT"
LABEL org.opencontainers.image.description="RSS to HTML converter"
LABEL org.opencontainers.image.licenses="GNU Affero GPL v3"
LABEL org.opencontainers.image.revision="$CI_COMMIT_SHA"
LABEL org.opencontainers.image.source=""
LABEL org.opencontainers.image.title="rss-to-html"
LABEL org.opencontainers.image.version="$CI_COMMIT_REF_NAME"

ADD src /opt/rss-to-html

ENTRYPOINT [ "/bin/bash" ]
