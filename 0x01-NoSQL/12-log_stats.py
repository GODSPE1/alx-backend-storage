#!/usr/bin/env python3
"""This module defines a function that count the number of logs"""


import pymongo
from pymongo import MongoClient


def get_nginx_log_stats(mongo_collection):
    """count total number of logs"""
    
    print(f"{mongo_collection.count()}) logs")

    print("Methods:")
    methods = 
    for method in ["GET", "POST", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = mongo_collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    get_nginx_log_stats(mongo_collection)
