from azure.storage.blob import BlobServiceClient

class BlobDataReader:
    CONNECTIONSTRING = 'DefaultEndpointsProtocol=https;AccountName=mlappdata;AccountKey=LiE9PRgvx0vl6HPkK9Kapw1lG71Ge7Gvi/gULY3bqk+v7jqO6E+Xjg/oOOA+eArGWYD4TWhN9p0I8qGlvNPY6Q==;EndpointSuffix=core.windows.net'
    CONTAINERNAME = 'datasets'
    FILENAME = 'heart.csv'

    def readData(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.CONNECTIONSTRING)
        container_client = blob_service_client.get_container_client(self.CONTAINERNAME)
        download_stream = container_client.download_blob(self.FILENAME)
        data = download_stream.readall()
        return data
