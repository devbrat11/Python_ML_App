from azure.storage.blob import BlockBlobService

class BlobDataReader:
    STORAGEACCOUNTNAME= 'mlappdata'
    STORAGEACCOUNTKEY= "LiE9PRgvx0vl6HPkK9Kapw1lG71Ge7Gvi/gULY3bqk+v7jqO6E+Xjg/oOOA+eArGWYD4TWhN9p0I8qGlvNPY6Q=="
    LOCALFILENAME= 'datasets/heart.csv'        
    CONTAINERNAME= 'datasets'
    BLOBNAME= 'heart.csv'

    def readData(self):
        blob_service = BlockBlobService(account_name=self.STORAGEACCOUNTNAME, account_key=self.STORAGEACCOUNTKEY)
        blobstring = blob_service.get_blob_to_text(self.CONTAINERNAME,self.BLOBNAME).content
        return blobstring