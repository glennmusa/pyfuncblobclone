import logging
import os
import azure.functions as func
from azure.storage.blob import BlobClient, BlobProperties, BlobType, ContentSettings


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    connection_string = os.environ["storage_connection_string"]
    account_key = os.environ["storage_account_key"]
    input_container = os.environ["input_container_name"]
    output_container = os.environ["output_container_name"]

    in_client = BlobClient.from_blob_url(myblob.uri, account_key)
    properties = in_client.get_blob_properties()
    name = properties.name
    content_type = properties.content_settings.content_type

    logging.info(f"Copying {name} from {input_container} to {output_container} with content-type {content_type}")

    out_client = BlobClient.from_connection_string(connection_string, output_container, name)
    out_client.upload_blob(
        data=myblob,
        blob_type=BlobType.BlockBlob,
        length=myblob.length,
        overwrite=True,
        content_settings=ContentSettings(content_type=content_type))

    logging.info(f"Uploaded complete for {output_container}/{name}")