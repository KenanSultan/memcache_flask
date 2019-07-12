## Installaion
    ### For memcache docker container
    1. Install memcached server on Debian/Ubuntu
        sudo apt-get install memcached
    1. Built an image
        docker build -t local/memcached:0.1 .
    2. Run the docker container
        docker run -itd --name memcached -p 11311:11211 -e MEMCACHED_MEMUSAGE=32 local/memcached:0.1

    ### For Flask currency project
    1. Create the virtual environment
        exemple: virtualenv -p python3 .py3
    2. Activate virtualenv
        exemple: source .py3/bin/activate
    3. Install packages
        pip3 install -r requirements.txt
    4. Run the project
        python currency.py