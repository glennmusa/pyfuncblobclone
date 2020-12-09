import logging
import os
import azure.functions as func
from azure.storage.blob import BlobClient, BlobProperties, BlobType, ContentSettings


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    input_account_key = os.environ["input_account_key"]
    input_container_name = os.environ["input_container_name"]

    output_connection_string = os.environ["output_connection_string"]
    output_container_name = os.environ["output_container_name"]

    logging.info(
        f"Instantiate client for {myblob.name} in {input_container_name}")

    in_client = BlobClient.from_blob_url(myblob.uri, input_account_key)

    logging.info(
        f"Get Blob Properties for {myblob.name} from {input_container_name}")

    properties = in_client.get_blob_properties()
    name = properties.name
    content_type = properties.content_settings.content_type

    logging.info(
        f"Instantiate client for {myblob.name} in {output_container_name}")

    out_client = BlobClient.from_connection_string(
        output_connection_string,
        output_container_name,
        name)

    logging.info(f"Copy {name}\n"
                 f"from {input_container_name} to {output_container_name}\n"
                 f"with content-type {content_type}")

    out_client.upload_blob(
        data=myblob,
        blob_type=BlobType.BlockBlob,
        length=myblob.length,
        overwrite=True,
        content_settings=ContentSettings(content_type=content_type))

    logging.info(f"Upload complete for {output_container_name}/{name}")
