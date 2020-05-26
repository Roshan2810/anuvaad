#!/bin/python
import os
import pymongo

mongo_client = os.environ.get('MONGO_CLIENT', 'mongodb://localhost:27017/')
mongo_alignment_db = os.environ.get('MONGO_ALIGNMENT_DB', 'anuvaad-etl-dataflow-pipeline')
mongo_alignment_col_jobs = os.environ.get('MONGO_WFMJOBS_COL', 'anuvaad-etl-wfm-jobs')
mongo_alignment_col_tasks = os.environ.get('MONGO_WFMTASKS_COL', 'anuvaad-etl-wfm-tasks')


class WFMRepository:

    def __init__(self):
        pass

    # Initialises and fetches mongo client
    def instantiate(self):
        client = pymongo.MongoClient(mongo_client)
        db = client[mongo_alignment_db]
        col = db[mongo_alignment_col_jobs]
        return col

    # Inserts the object into mongo collection
    def create_job(self, object_in):
        col = self.instantiate()
        col.insert_one(object_in)

    # Updates the object in the mongo collection
    def update_job(self, object_in, job_id):
        col = self.instantiate()
        col.replace_one(
            {"jobID": job_id},
            object_in
        )

    # Searches the object into mongo collection
    def search_job(self, job_id):
        col = self.instantiate()
        query = {"jobID" : job_id}
        res = col.find(query, {'_id': False})
        result = []
        for record in res:
            result.append(record)
        return result
