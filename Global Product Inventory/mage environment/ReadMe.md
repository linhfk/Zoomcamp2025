## Set up Mage environment
You can start by cloning the repo:
        
    git clone git clone https://github.com/linhfk/Zoomcamp2025.git 
Navigate to the repo:

    cd Global Product Inventory/mage environment
Rename dev.env to simply .env

Build the container
    docker compose build

Start the Docker container:
    docker compose up

Navigate to http://localhost:6789  
    
        ├── mage_data
        │  └── global-product-inventory
        ├── global-product-inventory
        │   ├── __pycache__
        │   ├── charts
        │   ├── custom
        │   ├── data_exporters
        │   ├── data_loaders
        │   ├── dbt
        │   ├── extensions
        │   ├── interactions
        │   ├── pipelines
        │   ├── scratchpads
        │   ├── transformers
        │   ├── utils
        │   ├── __init__.py
        │   ├── io_config.yaml
        │   ├── metadata.yaml
        │   └── requirements.txt
        ├── Dockerfile
        ├── README.md
        ├── dev.env
        ├── docker-compose.yml
 
