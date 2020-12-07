# pyfuncblobclone
This repo https://github.com/glennmusa/azfuncblobwithcontenttype, but make it Python

Uses the [Azure Storage BlobTrigger](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#example) to process a blob from the configured `input_container_name` in local.settings.json and makes use of the Azure Storage Blob SDK [BlobClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient?view=azure-python) to clone the blob with its content type to the configured `output_container_name` in local.settings.json.

## To get started:
1. Clone [./local.settings.json.sample](./local.settings.json.sample) and rename it to `local.settings.json`
1. Subtitute the settings values with your resources
1. All the fun stuff happens in [./pyfuncblobclone/\_\_init\_\_.py](pyfuncblobclone/__init__.py)
