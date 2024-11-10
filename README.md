# RSS-to-HTML

A podcast RSS feed to a static HTML website converter.


## Setup a configuration file

Create an appropriate config file, and edit it:

```bash
wget https://raw.githubusercontent.com/adrienbricchi/rss-to-html/refs/heads/master/src/application.cfg.dist \
    --output-document=application.cfg
```

## Run the conversion

### Using a Docker image

Link the input/output files variables.  
And make sure every output file actually exists, or the Docker engine will create some weird folders.

```bash
OUTPUT_FILE_PATH=./index.html
CONFIG_FILE_PATH=./application.cfg
touch ${OUTPUT_FILE_PATH} ${CONFIG_FILE_PATH}
```

Run the executable, that will update/overwrite the existing `index.html` file.

```bash
docker run \
    -v ${CONFIG_FILE_PATH?:}:/opt/rss-to-html/application.cfg \
    -v ${OUTPUT_FILE_PATH?:}:/opt/rss-to-html/index.html \
    adrienbricchi/rss-to-html:latest
```

### Using a local execution

Some prerequisites shall be set up:

- Python 3
- Pip

Then, the local dependencies:

```bash
pip install -r requirements.txt
```

Finally, we can run the executable:

```bash
cd .src/
python3 rss-to-html.py
```
