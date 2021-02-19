from google.cloud import bigquery

client = bigquery.Client()
query_job = client.query(
    """
    SELECT * FROM "myiotclouddb.IoTData.Sales"

    """
)

results = query_job.result()
for row in results:
    print("{} : {} views".format(row.url, row.view_count))
