#!/usr/bin/env python3
"""This module defines a function that count the number of logs"""

import pymongo
from pymongo import MongoClient


def get_nginx_log_stats(mongo_collection):
    """count total number of logs"""
    total_logs = mongo_collection.count()({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    status_check = mongo_collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    get_nginx_log_stats(mongo_collection)
